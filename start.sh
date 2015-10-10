#!/bin/bash
PATH=$PATH:/root/workplace/video_scrapy
export PATH
. /root/env_video/bin/activate
cd /root/workplace/video_scrapy
scrapy crawl iqiyi >> /root/workplace/video_scrapy/iqiyi.log
