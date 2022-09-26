from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import time
import re
import requests
import json
import requests
import json
from bs4 import BeautifulSoup
from threading import Thread


def get_routes(request):
    link = request.GET.get('v_id')

    if link:
        try:
            video = re.search(r'\d{19}', link)
            print("test")
            print(video.group())
            print("test")
            video_id = video.group()
            openudid = ''.join(random.sample('0123456789abcdef', 16))
            ts = int(time.time())
            uuid = ''.join(random.sample('01234567890123456', 16))
            tiktok_api_headers = {
                'user-agent': 'com.ss.android.ugc.trill/2613 (Linux; U; Android 10; en_US; Pixel 4; Build/QQ3A.200805.001; Cronet/58.0.2991.0)'
            }
            tiktok_api_link = 'https://api-h2.tiktokv.com/aweme/v1/feed/?aweme_id={}&version_name=26.1.3&version_code=2613&build_number=26.1.3&manifest_version_code=2613&update_version_code=2613&openudid={}&uuid={}&_rticket={}&ts={}&device_brand=Google&device_type=Pixel%204&device_platform=android&resolution=1080*1920&dpi=420&os_version=10&os_api=29&carrier_region=US&sys_region=US%C2%AEion=US&app_name=trill&app_language=en&language=en&timezone_name=America/New_York&timezone_offset=-14400&channel=googleplay&ac=wifi&mcc_mnc=310260&is_my_cn=0&aid=1180&ssmix=a&as=a1qwert123&cp=cbfhckdckkde1'.format(
                video_id, openudid, uuid, ts * 1000, ts)

            print(tiktok_api_link)
            response = requests.get(url=tiktok_api_link, headers=tiktok_api_headers).text
            result = json.loads(response)
            nwm_video_url = result["aweme_list"][0]["video"]["play_addr"]["url_list"]

            data = {"status": "true", 'data': nwm_video_url}
            routes = data

            return JsonResponse(routes, safe=False)
        except KeyError:
            return JsonResponse("We didn't find a required result... Please try again", safe=False)
        except AttributeError:
            return JsonResponse("Please give a valid video Id", safe=False)
    else:
        return JsonResponse("Please select a video", safe=False)


def video_list(request):
    cookie = request.GET.get("cookie")
    if cookie:
        def testing(params=''):
            links = []
            cookies = {"cookie": cookie}
            print("I am If")
            url = "https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F105.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7130525750311257602&device_platform=web_pc&focus_state=false&from_page=fyp&history_len=4&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=PK&referer=&region=PK&screen_height=720&screen_width=1280&tz_name=Asia%2FKarachi&webcast_language=en&msToken=_LK9VtxPkV6Qd87L40rTIjqJOderfXQbo1czPjNhWmkV2dsIYomyX79TIOHw7P0fv2eQWJi9V6CHrQjefGJHB-GWEcwjJy1gL3T37lJiqwcf7iqf4DVPVFIbSRBS7p_0sWgGxBp1J20kd2Pefg==&X-Bogus=DFSzswVLjyxANydASQM-jcYklTXR&_signature=_02B4Z6wo00001GYDPAwAAIDBuHVkqcP0F0xmAziAAHqf4f"
            res = requests.get(url, cookies=cookies)
            print("I am cookie")
            print(res.cookies)
            j_res = res.json()
            print(j_res["statusCode"])
            link_list = j_res["itemList"]
            for i in link_list:
                links.append(i['video']['playAddr'])
            print(links)
            return links

        routes = [
            {'URLS': testing()},
        ]
        print(routes)
        return JsonResponse(routes, safe=False)

    return JsonResponse("Please enter your cookie", safe=False)


def nwm(request):
    nwm_video_url = []

    try:
        def nowatermark(link):
            list1 = []
            for video in link:
                video_id = video
                openudid = ''.join(random.sample('0123456789abcdef', 16))
                ts = int(time.time())
                uuid = ''.join(random.sample('01234567890123456', 16))
                tiktok_api_headers = {
                    'user-agent': 'com.ss.android.ugc.trill/2613 (Linux; U; Android 10; en_US; Pixel 4; Build/QQ3A.200805.001; Cronet/58.0.2991.0)'
                }
                tiktok_api_link = 'https://api-h2.tiktokv.com/aweme/v1/feed/?aweme_id={}&version_name=26.1.3&version_code=2613&build_number=26.1.3&manifest_version_code=2613&update_version_code=2613&openudid={}&uuid={}&_rticket={}&ts={}&device_brand=Google&device_type=Pixel%204&device_platform=android&resolution=1080*1920&dpi=420&os_version=10&os_api=29&carrier_region=US&sys_region=US%C2%AEion=US&app_name=trill&app_language=en&language=en&timezone_name=America/New_York&timezone_offset=-14400&channel=googleplay&ac=wifi&mcc_mnc=310260&is_my_cn=0&aid=1180&ssmix=a&as=a1qwert123&cp=cbfhckdckkde1'.format(
                    video_id, openudid, uuid, ts * 1000, ts)

                response = requests.get(url=tiktok_api_link, headers=tiktok_api_headers).text
                result = json.loads(response)

                nwm_video_url.append(result["aweme_list"][0]["video"]["play_addr"]["url_list"][0])
                list1.append(result["aweme_list"][0]["video"]["play_addr"]["url_list"][0])
            return list1

        def testing(params=''):
            cover = []
            cookies = {
                "passport_csrf_token": "24d3cf05dcfd2eb4eb5e36bd0a1916f1; passport_csrf_token_default=24d3cf05dcfd2eb4eb5e36bd0a1916f1; passport_auth_status=497c66858d8e7c57518a5b1083bb35b7%2C373931e3ade6dda24eeea7d0aaa7401d; passport_auth_status_ss=497c66858d8e7c57518a5b1083bb35b7%2C373931e3ade6dda24eeea7d0aaa7401d; sid_guard=43431ad89f49cf40457e7f2ab1762493%7C1660712706%7C5183999%7CSun%2C+16-Oct-2022+05%3A05%3A05+GMT; uid_tt=ab9f72cdc085a6aef65541be31cb24cf9a2d732d965a3f2a032637f4a997eaa4; uid_tt_ss=ab9f72cdc085a6aef65541be31cb24cf9a2d732d965a3f2a032637f4a997eaa4; sid_tt=43431ad89f49cf40457e7f2ab1762493; sessionid=43431ad89f49cf40457e7f2ab1762493; sessionid_ss=43431ad89f49cf40457e7f2ab1762493; sid_ucp_v1=1.0.0-KDMzMmFhNGQ0OTM4NTc2MmQ1OTgyNzUxM2QyNGIxM2M1OWYxNzhiNGMKHwiCiLS0jpWg2GAQgu7xlwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiA0MzQzMWFkODlmNDljZjQwNDU3ZTdmMmFiMTc2MjQ5Mw; ssid_ucp_v1=1.0.0-KDMzMmFhNGQ0OTM4NTc2MmQ1OTgyNzUxM2QyNGIxM2M1OWYxNzhiNGMKHwiCiLS0jpWg2GAQgu7xlwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiA0MzQzMWFkODlmNDljZjQwNDU3ZTdmMmFiMTc2MjQ5Mw; store-idc=useast2a; store-country-code=pk; tt-target-idc=alisg; __tea_cache_tokens_1988={%22user_unique_id%22:%227130525750311257602%22%2C%22timestamp%22:1660714777509%2C%22_type_%22:%22default%22}; store-country-code-src=uid; MONITOR_WEB_ID=7a9e89be-892e-4384-b0f0-bc3191a4bae0; cmpl_token=AgQQAPO4F-RMpbCObg9uv907-JUuV6aLP4AzYMUqCg; tt_csrf_token=lZVGFB5E-TF1yZf56I4NQ6RyDsqIM9ol7Y9w; ttwid=1%7C5aHP662LIIjOmzFdf7FK29RhSiBxMhgny-m41kDwKi0%7C1662452610%7C24dcfa1244886aeb77e4336e2dcc55c7db1123cfda7b9c609bd1de2ba16a7062; ak_bmsc=DCA435C0F329AF4CF9DFA32F19EE85A4~000000000000000000000000000000~YAAQh8BBOun+KPyCAQAAyRPmEREfpX6MXiAiBKp1QbNdv28EVYKHO/CnViXil77pnIBLbA29C1xbLziLmhy7jmlEDOCHtmwlstjpXH70/01MhVjoqimIPzu+YsLMqZ98GGgv9VL+gxEy32xDOgPrbFGjl3Jo3pcnyku4vq2y5f09pzNr0PjEbzohfK/UZtz+6A2AoXgUtyglablJ6YHoKCWswPsFRioQrL16h+IDB7k38mHoibys31O3wgf/rp36XYpNMst1RdNRIVwRuGYUWvC9OWEq2Mgv92vSzj85srp7pmEXy3s3WH4TzDTZ73IP4waMAtq+qCNESw2VV0m9NoLwZWSxQnjGda84ydlS89rh9Z3ORy5e1Z7NVTXSFDO8Zcg5z5S+dIzU/A==; bm_sz=3C1D2D0E624A9819B508D3260B2EED97~YAAQlcBBOped//eCAQAAUQsBEhHZ+jifD29vln2Ja2TnnD0gsHZr02O3POLepI8M+xSpYbp9V8K+N0qIxPiNJ6ImUbmUhHnb30SOIYEHujaaNFADpMIUIZThQrgA56WkwKFIceqvLs7I10agCwAxKjA39oDlh7KSPdT/QrXTUBvBNEdBnVs1NYFxDdJv2/dGSYRWB4nqpSmUUbbECJsrsch4k3oVgrchFIIDWyGDQb98GmOJPn22m0NPDj4vHy/jPR0g45B44IinrHGf7W48/8skfpCmb1ud66/NcVnTO5+7LAdzZPtaLTV9xtqsUAxvOFL5XxcVBhD5d2Q=~4342338~3425072; passport_fe_beating_status=true; odin_tt=9d935743f1cacae91ef5209a4d9867199a706ba12ac35b9a8d7c566be4f7487551a0c7447fc0ae31994e97ae9896efd85bd182e3a4a59b7358eef190ac98196c901489493525d747f05f3116e3fef50a; bm_sv=1CA29B219EB0F21FA910F750BA94A181~YAAQlMBBOieL6vaCAQAAeftPEhEccRzhHKhf6JforPjfyVYU4UVyE42MXWzW54zxhIvMZH6UIRxjdg+neXxucPP5bxsz/ZW8HkTIAOrQnunLzWtvcCHgZVdlPpbnXEzg/dbxgaeSwzdxJQE2Y9kS8ImkLb0sEiMFfXe5C0iQVObY3ZZnRyWWtTPGT/eBdL0MZgej405iW6XJEhRsN9PLxn7pXG2dUedM5d4ovn1T7KE3c5uFrDMKqaqmnU3Ua5B6~1; msToken=_LK9VtxPkV6Qd87L40rTIjqJOderfXQbo1czPjNhWmkV2dsIYomyX79TIOHw7P0fv2eQWJi9V6CHrQjefGJHB-GWEcwjJy1gL3T37lJiqwcf7iqf4DVPVFIbSRBS7p_0sWgGxBp1J20kd2Pefg==; msToken=HEWyUQ15oy8pe4NQk1TSeeYmkjE5LJd6iYsYi2juZa-KxBuATDEXOby4p-OPiWBDGHg87YWXMZKQEhZmFs_QRjQnA3JoZvX4bjttCXZM1cVYjvTAV-N0whZsEk1F0WPMVbllLkAsFlyO8CIV7w==; _abck=9E413CE6509575293B9D2CD825C1DAA7~-1~YAAQjMBBOuPMEv2CAQAAXJ5TEggXuWL4OC7IFZZ8DDE1OHnL1TppIVSvp7LUi7w3HYT+2VXNuoXN8L4IAWybOk2sR8IKYw6IkH59ZyvRmYr7ctWzckCG2x9miBPVJvkTTR9+grgwUZ/1H/fYxKN5Pq5SczNW2mv3LcVhDdFI9KrCNJlMSjcCe74s891A2/cJwuC6boyRX/yih2o/56cCZ2RIXmGXmIGJJQUmdn61vMMGmoHSKf18HGNOruuobZbf/0Ue9NYeI0Nu7B+gU03NUapKpSk4TMuV1Zk8rush+AIheZjB5O4HDgcHLEOQODgMWKYASZwIx22usVLtNIKMOw0T04VcHkhFewTyO5RdE2g=~-1~-1~-1"}

            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}

            url = f"https://www.tiktok.com/tag/{params}"
            res = requests.get(url, cookies=cookies, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            a = soup.find("script", attrs={"id": "SIGI_STATE"})
            try:
                length = json.loads(a.text)['MobileItemModule']
                for i in length:
                    links_arr = length[i]['video']['playAddr']
                    link_id_arr = length[i]['id']
                    if "https://v16-webapp.tiktok.com" in links_arr:
                        if len(cover) < 5:
                            cover.append(link_id_arr)
                        else:
                            break

            except KeyError:
                pass
            # print(len(cover))
            # nowatermark(cover)
            nowatermark(cover)

            return cover

        data_list = testing("ronaldo")
        finaldata = nowatermark(data_list)
        data = {"status": "true", 'data': finaldata}
        routes = data
        return JsonResponse(routes, safe=False)
    except KeyError:
        return JsonResponse("We didn't find a required result... Please try again", safe=False)
    except AttributeError:
        return JsonResponse("Please give a valid video Id", safe=False)

