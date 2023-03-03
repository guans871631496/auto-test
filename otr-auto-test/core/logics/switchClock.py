import json
import time

from rwo.core.logics.api.ApiObject.LoginApi import LoginApi
from rwo.core.logics.api.SendRequest import SendRequest
from rwo.core.utils.log import logger
from rwo.config.project_path import host


class SwitchClockApi:

    def turn_on_the_clock(self,username,password,orderNumber,laborCodes):
        logger.info("调用api进行开钟")
        token = LoginApi().login(username,password)
        technicianHeader = {
            'Authorization': token,
            'Content-Type': 'application/json;charset=utf-8',
            'Vehicle-Business-Type': 'PC',
            'x-client-version': 'android-52.2.0',
            'user-agent': 'OTRMobileApp-52.2.0 android'}

        jobCardId = self.search_workshop_order(technicianHeader,orderNumber)
        logger.info(f"jobCardId:{jobCardId}")
        labourIdResult = self.search_labor_code_detail(technicianHeader,jobCardId)
        logger.info(f"labourIdResult:{labourIdResult}")
        labourIds = []
        for index in range(len(labourIdResult)):
            if labourIdResult[index]['laborCode'] in laborCodes and labourIdResult[index]['status'] == 'INITIATED':
                labourIds.append(labourIdResult[index]['id'])
        if len(labourIds) == 0:
            logger.info("No labor code can open the clock")
            return
        logger.info(f"labourIds:{labourIds}")

        laborItemIdsResult = self.search_technician_detail(technicianHeader,labourIds,jobCardId)
        logger.info(f"laborItemIdsResult:{laborItemIdsResult}")

        technicianId = laborItemIdsResult[0]['id']
        technicianName = laborItemIdsResult[0]['name']


        workStatusResult = self.search_works_status(technicianHeader,technicianId)
        logger.info(f"workStatusResult:{workStatusResult}")

        workStatus = None
        if workStatusResult['workStatus'] is not None :
            workStatus = workStatusResult['workStatus']['status']

        idUrl = host+'/api/sales-website/technician-idle-infos?technicianId=' + str(
            technicianId) + ''
        id = SendRequest().send_request('GET', idUrl, headers=technicianHeader).json()['id']
        logger.info(f"id:{id}")

        clockOnUrl = host + '/api/sales-website/job-cards/' + str(
           jobCardId) + '/labor-items/clock-on'
        clockOnBody = {
            "laborItemIds": labourIds,
            "laborItemStatus": "IN_PROGRESS",
            "technicianId": technicianId,
            "technicianName": technicianName
        }
        #'SIGN_OFF','CLOCK_ON'
        if workStatus == 'IDLE':
            clockOnUrl = host + '/api/sales-website/technician-idle-infos/' + str(
                id) + '/clock-off/clock-on-labor-items'
            clockOnBody = {
                "laborItemIds": labourIds,
                "laborItemStatus": "IN_PROGRESS",
                "technicianId": technicianId,
                "technicianName": technicianName,
                "jobCardId":jobCardId
            }
        clockOnResult = SendRequest().send_request('PATCH',clockOnUrl, data=json.dumps(clockOnBody),headers=technicianHeader)
        logger.info("开钟成功，api调用状态：%s" % clockOnResult.status_code)
        return clockOnResult.status_code


    def turn_off_the_clock(self,username,password,orderNumber,laborCodes):
        contToken = LoginApi().login(username, password)
        technicianHeader = {
            'Authorization': contToken,
            'Content-Type': 'application/json;charset=utf-8',
            'Vehicle-Business-Type': 'PC',
            'x-client-version': 'android-52.2.0',
            'user-agent': 'OTRMobileApp-52.2.0 android'}
        jobCardId = self.search_workshop_order(technicianHeader, orderNumber)
        logger.info(f"jobCardId:{jobCardId}")
        labourIdResult = self.search_labor_code_detail(technicianHeader, jobCardId)
        logger.info(f"labourIdResult:{labourIdResult}")
        labourIds = []
        technicianName = None
        technicianId = None
        for index in range(len(labourIdResult)):
            if labourIdResult[index]['laborCode'] in laborCodes and labourIdResult[index]['status'] == 'IN_PROGRESS':
                labourIds.append(labourIdResult[index]['id'])
                technicianName = labourIdResult[index]['technicianName']
                technicianId = labourIdResult[index]['technicianId']
        if len(labourIds) == 0:
            logger.info("No labor code can close the clock")
            return
        logger.info(f"labourIds:{labourIds}")

        workStatusResult = self.search_works_status(technicianHeader, technicianId)
        logger.info(f"workStatusResult:{workStatusResult}")

        workStatus = None
        if workStatusResult['workStatus'] is not None:
            workStatus = workStatusResult['workStatus']['status']

        clockOffUrl = host+'/api/sales-website/job-cards/'+str(jobCardId)+'/labor-items/clock-off/clock-on-idle'
        method = 'POST'
        clockOffBody = {
            "laborItemStatus": "COMPLETED",
            "laborItemIds": labourIds,
            "technicianId": technicianId,
            "technicianName": technicianName,
            "idleTypeId": 16
        }
        # if workStatus == 'CLOCK_ON':
        #     clockOffUrl = host+'/api/sales-website/job-cards/'+str(jobCardId)+'/labor-items/clock-off'
        #     method = 'PATCH'
        #     clockOffBody = {
        #         "laborItemStatus": "COMPLETED",
        #         "laborItemIds": labourIds,
        #         "technicianId": technicianId,
        #         "technicianName": technicianName,
        #     }
        clockOffResult = SendRequest().send_request(method, clockOffUrl, data=json.dumps(clockOffBody),headers=technicianHeader)
        logger.info("关钟成功,api调用状态：%s" % clockOffResult.status_code)


    def search_workshop_order(self,technicianHeader,orderNumber):
        jobCardIdUrl = host + '/api/sales-website/job-cards?keyword=' + orderNumber
        logger.info(f"jobCardIdUrl:{jobCardIdUrl}")
        jobCardResult = SendRequest().send_request('get', jobCardIdUrl, headers=technicianHeader).json()
        logger.info(f"jobCardResult:{jobCardResult}")
        count = 0
        while len(jobCardResult['today']) == 0 and count < 5:
            time.sleep(3)
            jobCardResult = SendRequest().send_request('get', jobCardIdUrl, headers=technicianHeader).json()
            count + 1
        jobCardId = jobCardResult['today'][0]['id']
        return jobCardId


    def search_labor_code_detail(self,technicianHeader,jobCardId):
        labourIdUrl = host + '/api/sales-website/job-cards/' + str(jobCardId) + '/labour-items'
        labourIdResult = SendRequest().send_request('get', labourIdUrl, headers=technicianHeader).json()
        return labourIdResult

    def search_technician_detail(self,technicianHeader,labourIds,jobCardId):
        labourIdsStr = ''
        for j in range(len(labourIds)):
            labourIdsStr += str(labourIds[j])
            if j < len(labourIds) - 1:
                labourIdsStr += ','
        laborItemIdsUrl = host + '/api/sales-website/technicians/available?laborItemIds=' + labourIdsStr + '&currentJobCardId=' + str(
            jobCardId) + ''
        laborItemIdsResult = SendRequest().send_request('GET', laborItemIdsUrl, headers=technicianHeader).json()
        return laborItemIdsResult
        logger.info(f"laborItemIdsResult:{laborItemIdsResult}")

    def search_works_status(self,technicianHeader,technicianId):
        workStatusUrl = host + '/api/sales-website/technicians/' + str(technicianId) + ''
        workStatusResult = SendRequest().send_request('GET', workStatusUrl, headers=technicianHeader).json()
        return workStatusResult

if __name__ == '__main__':
    s = SwitchClockApi()
    abc = s.turn_on_the_clock('KJCONT1', '789@Test', '22111614185gdg', '001155')
    s.turn_off_the_clock('KJCONT1', '789@Test', '22111614185gdg', ['001155','008503'])

