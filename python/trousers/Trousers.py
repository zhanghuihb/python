import requests

headers = {
    'cookie': 'COMPASS=drive=EMWoo_4FGkUACWuJV71e2HbqHBi1wCMA6FEXo-oNQqkb3EFQ1Vbm_vHL4UqeqJ0TXjR6sk7nBNv-C7scT65gOGCCWrXqOqZ05EqC-WI; HSID=ADkrr2-YbaPoPCpo9; SSID=AibJp1_l3e0FYURDy; APISID=dd2rjLnwHvVwk3ot/AxI9bL_ypbqbt2T8s; SAPISID=fcwBXOLCMHpt76rm/AXr8nqPcQlca07XeZ; __Secure-3PAPISID=fcwBXOLCMHpt76rm/AXr8nqPcQlca07XeZ; SEARCH_SAMESITE=CgQIpZEB; SID=4Qc1JhaRQnAO2S8oruQyt24Sa4kTYqD2LOBaA5SSGmkP5LhF5evXPGW2SCtJLJ1jQY8oPA.; __Secure-3PSID=4Qc1JhaRQnAO2S8oruQyt24Sa4kTYqD2LOBaA5SSGmkP5LhFc37KGpVA4BQIPox8rE8j0g.; 1P_JAR=2020-12-03-11; NID=204=C3pFywNiqZBbAN_5eGZ3jMgQRzBeB09oYuS4oHqZMCyv9GZU63GJhaozV8SKPXTqI0vm9N8babjFrjsCf-NT65W20JieNfHabRQsyOLRtKCAqC301YccP__E99QULWjqf9DNThWJipFnjT2bR_agS1l-gc-hw8D0fHtygD0FpNMq7GBcYzKxETZnRxnwWQKR27my6-IJknr2xXA14ZXTaRdY1lcmKS1R8Jban3zVrz83FiEA_kjjpxwktw; SIDCC=AJi4QfF3zqUfe4fl2E57rNGzHS6YkVmufB131_SwmZP9_KDp2LKN09cp6FfKAYqBiDjVE_womQ; __Secure-3PSIDCC=AJi4QfGEG9xCnUZKZ96ehuWQdd52Z_adUrhKgMKYmTeRy7reC71hY41MtGQwNkpDpxlLlTQrpUo',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
    ':authority': 'drive.google.com',
    'x-chrome-connected': 'source=Chrome,id=104355450850890501488,mode=0,enable_account_consistency=false,supervised=false,consistency_enabled_by_default=false',
    'x-client-data': 'CKq1yQEIhbbJAQiktskBCMS2yQEIqZ3KAQjruMoBCPbHygEItMvKAQi8z8oBCNzVygEIi5nLARiKwcoB',
    ':method': 'GET',
    ':path': '/drive/folders/1p4ZTlvbP_6SzKl6SAUrh5EGrFrNj_ZTo',
    ':scheme': 'https'
}
response = requests.get("https://drive.google.com/drive/folders/1p4ZTlvbP_6SzKl6SAUrh5EGrFrNj_ZTo", headers=headers)
print(response.text)