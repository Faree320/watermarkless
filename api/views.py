from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import asyncio
# from TikTokApi import TikTokApi
import math
from .serializers import tiktok_api
import random
import time, datetime
import urllib
import re

import requests


def get_routes(request):
    link = request.GET.get('v_id')

    if link:
        try:
            video = re.search(r'\d{19}', link)
            print("test")
            print(video.group())
            print("test")
            video_id = video.group()

            def generate_device_id():
                a = (''.join(str(random.randint(0, 9)) for _ in range(19)))
                return a

            def generate_base62(length):
                base62 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
                b = (''.join(str(random.choice(base62)) for _ in range(length)))
                return b

            def request_aweme(path):
                headers = {'User-Agent': 'okhttp', }
                time_now = int(time.time() * 1000)
                request_url = 'https://api-t2.tiktokv.com' + path + '&region=US' + '&ts=' + str(
                    math.floor(
                        time_now / 1000)) + '&timezone_name=Etc%2FGMT' + '&device_type=Pixel%20' + generate_base62(
                    8) + '&iid=' + generate_device_id() + '&locale=en' + '&app_type=normal' + '&resolution=1080*1920' + '&aid=1180' + '&app_name=musical_ly' + '&_rticket=' + str(
                    time_now) + '&device_platform=android' + '&version_code=100000' + '&dpi=441' + '&cpu_support64=false' + '&sys_region=US' + '&timezone_offset=0' + '&device_id=' + generate_device_id() + '&pass-route=1' + '&device_brand=google' + '&os_version=8.0.0' + '&op_region=US' + '&app_language=en' + '&pass-region=1' + '&language=en' + '&channel=googleplay'
                res = requests.get(request_url, headers=headers)
                return res

            def request_video_detail(id):
                return request_aweme('/aweme/v1/aweme/detail/?aweme_id=' + id)

            def final_result():
                example_data = request_video_detail(video_id)
                data = example_data.json()
                # secretID = data["aweme_detail"]["video"]["play_addr"]["uri"]
                watermarklessURLs = data["aweme_detail"]["video"]["play_addr"]["url_list"]
                return watermarklessURLs

            routes = [
                {'URLS': final_result()},
            ]
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
