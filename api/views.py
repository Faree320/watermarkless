from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import time
import re
import requests
import json


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
            nwm_video_url = result["aweme_list"][0]["video"]["play_addr"]["url_list"][0]

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
