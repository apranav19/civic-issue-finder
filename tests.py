#!/usr/bin/env python
# -*- coding: utf8 -*-

import unittest, requests, json, os
from datetime import datetime, timedelta
from urlparse import urlparse

from httmock import response, HTTMock, all_requests
from flask.ext.testing import TestCase
from app import app

class AppTestCase(TestCase):

  def create_app(self):
    # This method is required by flask.ext.testing.TestCase. It is called
    # before setUp().
    return app

  @all_requests
  def response_content(self, url, request):

    if url.geturl() == 'http://codeforamerica.org/api/organizations?per_page=200':
      return response(200, ''' {"objects":[{"all_events":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/events","all_issues":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/issues","all_projects":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/projects","all_stories":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/stories","api_url":"http://codeforamerica.org/api/organizations/Code-for-South-Africa","city":"Cape Town, South Africa","current_events":[],"current_projects":[{"api_url":"http://codeforamerica.org/api/projects/306","categories":null,"code_url":"https://github.com/Code4SA/censusreporter","description":"Fork of Census Reporter for showing South African census data","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/56477?v=1","contributions":704,"html_url":"https://github.com/ryanpitts","login":"ryanpitts","owner":false,"url":"https://api.github.com/users/ryanpitts"},{"avatar_url":"https://avatars.githubusercontent.com/u/4178542?v=1","contributions":133,"html_url":"https://github.com/longhotsummer","login":"longhotsummer","owner":false,"url":"https://api.github.com/users/longhotsummer"},{"avatar_url":"https://avatars.githubusercontent.com/u/261584?v=1","contributions":108,"html_url":"https://github.com/iandees","login":"iandees","owner":false,"url":"https://api.github.com/users/iandees"},{"avatar_url":"https://avatars.githubusercontent.com/u/3660183?v=1","contributions":76,"html_url":"https://github.com/petrus-jvrensburg","login":"petrus-jvrensburg","owner":false,"url":"https://api.github.com/users/petrus-jvrensburg"},{"avatar_url":"https://avatars.githubusercontent.com/u/46313?v=1","contributions":75,"html_url":"https://github.com/JoeGermuska","login":"JoeGermuska","owner":false,"url":"https://api.github.com/users/JoeGermuska"},{"avatar_url":"https://avatars.githubusercontent.com/u/588701?v=1","contributions":67,"html_url":"https://github.com/Rizziepit","login":"Rizziepit","owner":false,"url":"https://api.github.com/users/Rizziepit"},{"avatar_url":"https://avatars.githubusercontent.com/u/3248981?v=1","contributions":16,"html_url":"https://github.com/SaraSchnadt","login":"SaraSchnadt","owner":false,"url":"https://api.github.com/users/SaraSchnadt"}],"contributors_url":"https://api.github.com/repos/Code4SA/censusreporter/contributors","created_at":"2014-04-08T09:17:44Z","description":"Fork of Census Reporter for showing South African census data","forks_count":2,"homepage":"http://mma-dashboard.code4sa.org","html_url":"https://github.com/Code4SA/censusreporter","id":18552242,"language":"Python","name":"censusreporter","open_issues":1,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/4387576?v=1","html_url":"https://github.com/Code4SA","login":"Code4SA","type":"Organization"},"participation":[30,27,33,20,24,12,20,17,17,10,21,15,3,9,11,13,17,14,6,11,17,4,12,22,11,15,39,41,8,36,20,14,12,16,25,33,46,59,43,42,67,47,25,15,12,12,1,21,1,4,2,4],"pushed_at":"2014-07-30T17:45:59Z","updated_at":"2014-07-31T15:25:17Z","watchers_count":4},"id":306,"issues":[{"api_url":"http://codeforamerica.org/api/issues/933","body":"enables this view: http://censusreporter.org/profiles/?q=new+york","html_url":"https://github.com/Code4SA/censusreporter/issues/31","id":933,"labels":[],"project_id":306,"title":"Enable GeographySearchView from upstream"}],"last_updated":"Thu, 31 Jul 2014 15:25:17 GMT","last_updated_issues":"209463da79c53a04d71dc406322b3add","link_url":"http://mma-dashboard.code4sa.org","name":"censusreporter","organization_name":"Code for South Africa","type":null},{"api_url":"http://codeforamerica.org/api/projects/327","categories":null,"code_url":"https://github.com/Code4SA/odac-idp","description":"Demo Web application for browsing through information relating to the government's numerous Integrated Development Plans.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/3660183?v=1","contributions":42,"html_url":"https://github.com/petrus-jvrensburg","login":"petrus-jvrensburg","owner":false,"url":"https://api.github.com/users/petrus-jvrensburg"}],"contributors_url":"https://api.github.com/repos/Code4SA/odac-idp/contributors","created_at":"2014-01-20T06:48:13Z","description":"Demo Web application for browsing through information relating to the government's numerous Integrated Development Plans.","forks_count":0,"homepage":null,"html_url":"https://github.com/Code4SA/odac-idp","id":16063180,"language":"JavaScript","name":"odac-idp","open_issues":0,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/4387576?v=1","html_url":"https://github.com/Code4SA","login":"Code4SA","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,2,2,0,0,7,0,1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],"pushed_at":"2014-07-30T15:17:26Z","updated_at":"2014-07-30T15:17:26Z","watchers_count":0},"id":327,"issues":[],"last_updated":"Wed, 30 Jul 2014 15:17:26 GMT","last_updated_issues":"c4857e22d8292808ff009e4e676df323","link_url":null,"name":"odac-idp","organization_name":"Code for South Africa","type":null},{"api_url":"http://codeforamerica.org/api/projects/308","categories":null,"code_url":"https://github.com/Code4SA/Domestic-Workers","description":"","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/8087538?v=1","contributions":65,"html_url":"https://github.com/shakermaker","login":"shakermaker","owner":false,"url":"https://api.github.com/users/shakermaker"},{"avatar_url":"https://avatars.githubusercontent.com/u/3660183?v=1","contributions":44,"html_url":"https://github.com/petrus-jvrensburg","login":"petrus-jvrensburg","owner":false,"url":"https://api.github.com/users/petrus-jvrensburg"}],"contributors_url":"https://api.github.com/repos/Code4SA/Domestic-Workers/contributors","created_at":"2014-07-29T09:12:08Z","description":"","forks_count":0,"homepage":null,"html_url":"https://github.com/Code4SA/Domestic-Workers","id":22374132,"language":"JavaScript","name":"Domestic-Workers","open_issues":0,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/4387576?v=1","html_url":"https://github.com/Code4SA","login":"Code4SA","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,35,51],"pushed_at":"2014-07-31T14:33:23Z","updated_at":"2014-07-29T09:48:36Z","watchers_count":0},"id":308,"issues":[],"last_updated":"Tue, 29 Jul 2014 09:48:36 GMT","last_updated_issues":null,"link_url":null,"name":"Domestic-Workers","organization_name":"Code for South Africa","type":null}],"current_stories":[],"events_url":"http://www.meetup.com/Code-for-South-Africa-Hackers","last_updated":1406830057,"latitude":-33.9205,"longitude":18.4212,"name":"Code for South Africa","past_events":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/past_events","projects_list_url":"https://github.com/code4sa","rss":"","started_on":"2014-07-30","type":"Code for All","upcoming_events":"http://codeforamerica.org/api/organizations/Code-for-South-Africa/upcoming_events","website":"http://www.code4sa.org/"},{"all_events":"http://codeforamerica.org/api/organizations/Open-Nebraska/events","all_issues":"http://codeforamerica.org/api/organizations/Open-Nebraska/issues","all_projects":"http://codeforamerica.org/api/organizations/Open-Nebraska/projects","all_stories":"http://codeforamerica.org/api/organizations/Open-Nebraska/stories","api_url":"http://codeforamerica.org/api/organizations/Open-Nebraska","city":"Omaha, NE","current_events":[{"api_url":"http://codeforamerica.org/api/events/2755","created_at":"2014-07-31 10:57:01","description":null,"end_time":null,"event_url":"http://www.meetup.com/Open-Nebraska-Meetup/events/198178692/","id":2755,"location":null,"name":"Civic Hacking Workshop @ Interface","organization_name":"Open Nebraska","start_time":"2014-08-02 08:00:00 -0500"},{"api_url":"http://codeforamerica.org/api/events/104","created_at":"2014-07-06 08:59:55","description":null,"end_time":null,"event_url":"http://www.meetup.com/Open-Nebraska-Meetup/events/193291472/","id":104,"location":null,"name":"Open Nebraska August Meetup","organization_name":"Open Nebraska","start_time":"2014-08-04 18:00:00 -0500"}],"current_projects":[{"api_url":"http://codeforamerica.org/api/projects/31","categories":null,"code_url":"https://github.com/opennebraska/ne_state_restaurant_inspections","description":"State restaurant inspections for Nebraska","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/118361?v=1","contributions":172,"html_url":"https://github.com/rnelson","login":"rnelson","owner":false,"url":"https://api.github.com/users/rnelson"},{"avatar_url":"https://avatars.githubusercontent.com/u/4909406?v=1","contributions":60,"html_url":"https://github.com/dlipskey","login":"dlipskey","owner":false,"url":"https://api.github.com/users/dlipskey"},{"avatar_url":"https://avatars.githubusercontent.com/u/163745?v=1","contributions":3,"html_url":"https://github.com/natebenes","login":"natebenes","owner":false,"url":"https://api.github.com/users/natebenes"}],"contributors_url":"https://api.github.com/repos/opennebraska/ne_state_restaurant_inspections/contributors","created_at":"2014-05-09T20:49:43Z","description":"State restaurant inspections for Nebraska","forks_count":0,"homepage":null,"html_url":"https://github.com/opennebraska/ne_state_restaurant_inspections","id":19625143,"language":"JavaScript","name":"ne_state_restaurant_inspections","open_issues":0,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/5042049?v=1","html_url":"https://github.com/opennebraska","login":"opennebraska","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,10,2,1,24,20,25,11,19,18,0,3,0,2,0,2,2,1,0,2,1,1,1,2,2,0,0,0,0,0,0,0,1,2,0,0],"pushed_at":"2014-07-14T13:20:49Z","updated_at":"2014-07-09T12:11:19Z","watchers_count":0},"id":31,"issues":[],"last_updated":"Wed, 09 Jul 2014 12:11:19 GMT","last_updated_issues":null,"link_url":null,"name":"ne_state_restaurant_inspections","organization_name":"Open Nebraska","type":null},{"api_url":"http://codeforamerica.org/api/projects/35","categories":null,"code_url":"https://github.com/opennebraska/transitparty","description":"Visualizing the Omaha Metro transit system","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/163745?v=1","contributions":15,"html_url":"https://github.com/natebenes","login":"natebenes","owner":false,"url":"https://api.github.com/users/natebenes"},{"avatar_url":"https://avatars.githubusercontent.com/u/4648091?v=1","contributions":1,"html_url":"https://github.com/rstav","login":"rstav","owner":false,"url":"https://api.github.com/users/rstav"}],"contributors_url":"https://api.github.com/repos/opennebraska/transitparty/contributors","created_at":"2013-11-23T19:02:14Z","description":"Visualizing the Omaha Metro transit system","forks_count":1,"homepage":"http://transitparty.opennebraska.io/","html_url":"https://github.com/opennebraska/transitparty","id":14648485,"language":"JavaScript","name":"transitparty","open_issues":1,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/5042049?v=1","html_url":"https://github.com/opennebraska","login":"opennebraska","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2013-12-28T21:17:05Z","updated_at":"2014-06-01T01:18:21Z","watchers_count":3},"id":35,"issues":[{"api_url":"http://codeforamerica.org/api/issues/66","body":"I have an issue. No, just kidding. Trying to illustrate waffle. Will delete in a sec. ","html_url":"https://github.com/opennebraska/transitparty/issues/4","id":66,"labels":[],"project_id":35,"title":"Sample issue"}],"last_updated":"Sun, 01 Jun 2014 01:18:21 GMT","last_updated_issues":"ce3136a8dadb034ead97eadf6e466c86","link_url":"http://transitparty.opennebraska.io/","name":"transitparty","organization_name":"Open Nebraska","type":null},{"api_url":"http://codeforamerica.org/api/projects/32","categories":null,"code_url":"https://github.com/opennebraska/openrfps-scrapers","description":"Scraping government contracting opportunities.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/1270317?v=1","contributions":76,"html_url":"https://github.com/adamjacobbecker","login":"adamjacobbecker","owner":false,"url":"https://api.github.com/users/adamjacobbecker"},{"avatar_url":"https://avatars.githubusercontent.com/u/6753753?v=1","contributions":7,"html_url":"https://github.com/eabh","login":"eabh","owner":false,"url":"https://api.github.com/users/eabh"},{"avatar_url":"https://avatars.githubusercontent.com/u/8958?v=1","contributions":7,"html_url":"https://github.com/cjoh","login":"cjoh","owner":false,"url":"https://api.github.com/users/cjoh"},{"avatar_url":"https://avatars.githubusercontent.com/u/534176?v=1","contributions":6,"html_url":"https://github.com/jasonlally","login":"jasonlally","owner":false,"url":"https://api.github.com/users/jasonlally"},{"avatar_url":"https://avatars.githubusercontent.com/u/4350125?v=1","contributions":6,"html_url":"https://github.com/mkessy","login":"mkessy","owner":false,"url":"https://api.github.com/users/mkessy"},{"avatar_url":"https://avatars.githubusercontent.com/u/152?v=1","contributions":1,"html_url":"https://github.com/al3x","login":"al3x","owner":false,"url":"https://api.github.com/users/al3x"}],"contributors_url":"https://api.github.com/repos/opennebraska/openrfps-scrapers/contributors","created_at":"2014-03-06T14:37:41Z","description":"Scraping government contracting opportunities.","forks_count":0,"homepage":"openrfps.org","html_url":"https://github.com/opennebraska/openrfps-scrapers","id":17480653,"language":"CoffeeScript","name":"openrfps-scrapers","open_issues":0,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/5042049?v=1","html_url":"https://github.com/opennebraska","login":"opennebraska","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,84,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2014-03-17T15:17:17Z","updated_at":"2014-04-05T18:36:53Z","watchers_count":0},"id":32,"issues":[],"last_updated":"Sat, 05 Apr 2014 18:36:53 GMT","last_updated_issues":null,"link_url":"openrfps.org","name":"openrfps-scrapers","organization_name":"Open Nebraska","type":null}],"current_stories":[{"api_url":"http://codeforamerica.org/api/stories/7","id":7,"link":"http://opennebraska.io/hack-omaha-project-contains-to-fill-the-belly-of-hope-for-open-data/","organization_name":"Open Nebraska","title":"H.O. project continues to fill our belly with hope for Open Data in Nebraska","type":"blog"}],"events_url":"http://www.meetup.com/Open-Nebraska-Meetup/","last_updated":1406830150,"latitude":41.2524,"longitude":-95.998,"name":"Open Nebraska","past_events":"http://codeforamerica.org/api/organizations/Open-Nebraska/past_events","projects_list_url":"https://github.com/opennebraska","rss":"","started_on":"2014-07-30","type":"stage1","upcoming_events":"http://codeforamerica.org/api/organizations/Open-Nebraska/upcoming_events","website":"http://opennebraska.io/"}],"pages":{"last":"http://codeforamerica.org/api/organizations?per_page=2&page=42","next":"http://codeforamerica.org/api/organizations?per_page=2&page=2"},"total":84} ''')
    
    elif url.geturl() == 'http://codeforamerica.org/api/issues/labels/enhancement?per_page=100':
      return response(200, ''' {"objects":[{"api_url":"http://codeforamerica.org/api/issues/3","body":"Add facility to provide help for filling out the forms. This page could provide the content: http://www.ethics.state.tx.us/forms/COH_ins.htm","html_url":"https://github.com/open-austin/tecfiler/issues/28","id":3,"labels":[{"color":"84b6eb","name":"enhancement","url":"https://api.github.com/repos/open-austin/tecfiler/labels/enhancement"}],"project":{"api_url":"http://codeforamerica.org/api/projects/1","categories":"elections","code_url":"https://github.com/open-austin/tecfiler","description":"A system for filing campaign finance reports required by the Texas Ethics Commission. Open source and can be deployed anywhere in Texas.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/1208924?v=1","contributions":80,"html_url":"https://github.com/chip-rosenthal","login":"chip-rosenthal","owner":false,"url":"https://api.github.com/users/chip-rosenthal"},{"avatar_url":"https://avatars.githubusercontent.com/u/9507?v=1","contributions":21,"html_url":"https://github.com/hdaniel","login":"hdaniel","owner":false,"url":"https://api.github.com/users/hdaniel"},{"avatar_url":"https://avatars.githubusercontent.com/u/40304?v=1","contributions":9,"html_url":"https://github.com/royw","login":"royw","owner":false,"url":"https://api.github.com/users/royw"}],"contributors_url":"https://api.github.com/repos/open-austin/tecfiler/contributors","created_at":"2012-08-22T05:33:53Z","description":"A system for filing campaign finance reports required by the Texas Ethics Commission. Open source and can be deployed anywhere in Texas.","forks_count":1,"homepage":"","html_url":"https://github.com/open-austin/tecfiler","id":5505162,"language":"Ruby","name":"tecfiler","open_issues":16,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/970084?v=1","html_url":"https://github.com/open-austin","login":"open-austin","type":"Organization"},"participation":[0,0,0,0,1,6,8,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2014-02-01T14:52:37Z","updated_at":"2014-04-26T00:03:09Z","watchers_count":4},"id":1,"last_updated":"Sat, 26 Apr 2014 00:03:09 GMT","last_updated_issues":"503a3a8aea164537eba22df793284ce8","link_url":"","name":"TEC Filer","organization_name":"Open Austin","type":"web service"},"title":"add help facility"},{"api_url":"http://codeforamerica.org/api/issues/18","body":"Make sure about page addresses issue of residents that do not get ARR pickup service (e.g. apartments).","html_url":"https://github.com/open-austin/austin-recycles/issues/23","id":18,"labels":[{"color":"84b6eb","name":"enhancement","url":"https://api.github.com/repos/open-austin/austin-recycles/labels/enhancement"},{"color":"fef2c0","name":"hack","url":"https://api.github.com/repos/open-austin/austin-recycles/labels/hack"}],"project":{"api_url":"http://codeforamerica.org/api/projects/2","categories":"environment, recycle, waste management","code_url":"https://github.com/open-austin/austin-recycles","description":"Application and web service that provides trash and recycling pickup information for the City of Austin.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/1208924?v=1","contributions":32,"html_url":"https://github.com/chip-rosenthal","login":"chip-rosenthal","owner":false,"url":"https://api.github.com/users/chip-rosenthal"},{"avatar_url":"https://avatars.githubusercontent.com/u/3833093?v=1","contributions":7,"html_url":"https://github.com/travishohl","login":"travishohl","owner":false,"url":"https://api.github.com/users/travishohl"},{"avatar_url":"https://avatars.githubusercontent.com/u/9507?v=1","contributions":6,"html_url":"https://github.com/hdaniel","login":"hdaniel","owner":false,"url":"https://api.github.com/users/hdaniel"},{"avatar_url":"https://avatars.githubusercontent.com/u/114688?v=1","contributions":3,"html_url":"https://github.com/khit","login":"khit","owner":false,"url":"https://api.github.com/users/khit"}],"contributors_url":"https://api.github.com/repos/open-austin/austin-recycles/contributors","created_at":"2013-02-26T21:06:19Z","description":"Application and web service that provides trash and recycling pickup information for the City of Austin.","forks_count":7,"homepage":"http://austin-recycles.open-austin.org/","html_url":"https://github.com/open-austin/austin-recycles","id":8442001,"language":"JavaScript","name":"austin-recycles","open_issues":8,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/970084?v=1","html_url":"https://github.com/open-austin","login":"open-austin","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],"pushed_at":"2014-06-22T20:03:22Z","updated_at":"2014-06-22T20:03:22Z","watchers_count":3},"id":2,"last_updated":"Sun, 22 Jun 2014 20:03:22 GMT","last_updated_issues":"496b6150e6b304716240d2c7cb7c8bdd","link_url":"http://austin-recycles.open-austin.org/","name":"Austin Recycles","organization_name":"Open Austin","type":"web service"},"title":"help for non-service residents"}],"pages":{"last":"http://codeforamerica.org/api/issues/labels/enhancement?page=301&per_page=2","next":"http://codeforamerica.org/api/issues/labels/enhancement?page=2&per_page=2"},"total":601} ''')
    
    elif url.geturl() == 'http://codeforamerica.org/api/issues/labels/enhancement,hack?per_page=100':
      return response(200, ''' {"objects":[{"api_url":"http://codeforamerica.org/api/issues/3","body":"Add facility to provide help for filling out the forms. This page could provide the content: http://www.ethics.state.tx.us/forms/COH_ins.htm","html_url":"https://github.com/open-austin/tecfiler/issues/28","id":3,"labels":[{"color":"84b6eb","name":"enhancement","url":"https://api.github.com/repos/open-austin/tecfiler/labels/enhancement"}],"project":{"api_url":"http://codeforamerica.org/api/projects/1","categories":"elections","code_url":"https://github.com/open-austin/tecfiler","description":"A system for filing campaign finance reports required by the Texas Ethics Commission. Open source and can be deployed anywhere in Texas.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/1208924?v=1","contributions":80,"html_url":"https://github.com/chip-rosenthal","login":"chip-rosenthal","owner":false,"url":"https://api.github.com/users/chip-rosenthal"},{"avatar_url":"https://avatars.githubusercontent.com/u/9507?v=1","contributions":21,"html_url":"https://github.com/hdaniel","login":"hdaniel","owner":false,"url":"https://api.github.com/users/hdaniel"},{"avatar_url":"https://avatars.githubusercontent.com/u/40304?v=1","contributions":9,"html_url":"https://github.com/royw","login":"royw","owner":false,"url":"https://api.github.com/users/royw"}],"contributors_url":"https://api.github.com/repos/open-austin/tecfiler/contributors","created_at":"2012-08-22T05:33:53Z","description":"A system for filing campaign finance reports required by the Texas Ethics Commission. Open source and can be deployed anywhere in Texas.","forks_count":1,"homepage":"","html_url":"https://github.com/open-austin/tecfiler","id":5505162,"language":"Ruby","name":"tecfiler","open_issues":16,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/970084?v=1","html_url":"https://github.com/open-austin","login":"open-austin","type":"Organization"},"participation":[0,0,0,0,1,6,8,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2014-02-01T14:52:37Z","updated_at":"2014-04-26T00:03:09Z","watchers_count":4},"id":1,"last_updated":"Sat, 26 Apr 2014 00:03:09 GMT","last_updated_issues":"503a3a8aea164537eba22df793284ce8","link_url":"","name":"TEC Filer","organization_name":"Open Austin","type":"web service"},"title":"add help facility"},{"api_url":"http://codeforamerica.org/api/issues/17","body":"Usability issue where a visitor might enter an address and then click the START button. Some possible solutions: * Rename START to FIND ME.* If a person enters an address and clicks START, treat it as SEARCH.","html_url":"https://github.com/open-austin/austin-recycles/issues/24","id":17,"labels":[{"color":"fc2929","name":"bug","url":"https://api.github.com/repos/open-austin/austin-recycles/labels/bug"},{"color":"fef2c0","name":"hack","url":"https://api.github.com/repos/open-austin/austin-recycles/labels/hack"}],"project":{"api_url":"http://codeforamerica.org/api/projects/2","categories":"environment, recycle, waste management","code_url":"https://github.com/open-austin/austin-recycles","description":"Application and web service that provides trash and recycling pickup information for the City of Austin.","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/1208924?v=1","contributions":32,"html_url":"https://github.com/chip-rosenthal","login":"chip-rosenthal","owner":false,"url":"https://api.github.com/users/chip-rosenthal"},{"avatar_url":"https://avatars.githubusercontent.com/u/3833093?v=1","contributions":7,"html_url":"https://github.com/travishohl","login":"travishohl","owner":false,"url":"https://api.github.com/users/travishohl"},{"avatar_url":"https://avatars.githubusercontent.com/u/9507?v=1","contributions":6,"html_url":"https://github.com/hdaniel","login":"hdaniel","owner":false,"url":"https://api.github.com/users/hdaniel"},{"avatar_url":"https://avatars.githubusercontent.com/u/114688?v=1","contributions":3,"html_url":"https://github.com/khit","login":"khit","owner":false,"url":"https://api.github.com/users/khit"}],"contributors_url":"https://api.github.com/repos/open-austin/austin-recycles/contributors","created_at":"2013-02-26T21:06:19Z","description":"Application and web service that provides trash and recycling pickup information for the City of Austin.","forks_count":7,"homepage":"http://austin-recycles.open-austin.org/","html_url":"https://github.com/open-austin/austin-recycles","id":8442001,"language":"JavaScript","name":"austin-recycles","open_issues":8,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/970084?v=1","html_url":"https://github.com/open-austin","login":"open-austin","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],"pushed_at":"2014-06-22T20:03:22Z","updated_at":"2014-06-22T20:03:22Z","watchers_count":3},"id":2,"last_updated":"Sun, 22 Jun 2014 20:03:22 GMT","last_updated_issues":"496b6150e6b304716240d2c7cb7c8bdd","link_url":"http://austin-recycles.open-austin.org/","name":"Austin Recycles","organization_name":"Open Austin","type":"web service"},"title":"usability issue with START button"}],"pages":{"last":"http://codeforamerica.org/api/issues/labels/enhancement,hack?page=310&per_page=2","next":"http://codeforamerica.org/api/issues/labels/enhancement,hack?page=2&per_page=2"},"total":619} ''')
    
    elif url.geturl() == 'http://codeforamerica.org/api/organizations/Code%20for%20San%20Francisco/issues/labels/enhancement,hack?per_page=100':
      return response(200, ''' {"objects":[{"api_url":"http://codeforamerica.org/api/issues/81","body":"Start writing tests. ","html_url":"https://github.com/sfbrigade/ballot_initiatives/issues/7","id":81,"labels":[{"color":"84b6eb","name":"enhancement","url":"https://api.github.com/repos/sfbrigade/ballot_initiatives/labels/enhancement"}],"project":{"api_url":"http://codeforamerica.org/api/projects/108","categories":null,"code_url":"https://github.com/sfbrigade/ballot_initiatives","description":"","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/613334?v=1","contributions":16,"html_url":"https://github.com/andyhull","login":"andyhull","owner":false,"url":"https://api.github.com/users/andyhull"},{"avatar_url":"https://avatars.githubusercontent.com/u/1056580?v=1","contributions":10,"html_url":"https://github.com/mluedke2","login":"mluedke2","owner":false,"url":"https://api.github.com/users/mluedke2"},{"avatar_url":"https://avatars.githubusercontent.com/u/1231630?v=1","contributions":4,"html_url":"https://github.com/seanknox","login":"seanknox","owner":false,"url":"https://api.github.com/users/seanknox"},{"avatar_url":"https://avatars.githubusercontent.com/u/534176?v=1","contributions":3,"html_url":"https://github.com/jasonlally","login":"jasonlally","owner":false,"url":"https://api.github.com/users/jasonlally"},{"avatar_url":"https://avatars.githubusercontent.com/u/930705?v=1","contributions":1,"html_url":"https://github.com/charliemoseley","login":"charliemoseley","owner":false,"url":"https://api.github.com/users/charliemoseley"},{"avatar_url":"https://avatars.githubusercontent.com/u/1310178?v=1","contributions":1,"html_url":"https://github.com/julianeon","login":"julianeon","owner":false,"url":"https://api.github.com/users/julianeon"},{"avatar_url":"https://avatars.githubusercontent.com/u/567099?v=1","contributions":1,"html_url":"https://github.com/nmu","login":"nmu","owner":false,"url":"https://api.github.com/users/nmu"}],"contributors_url":"https://api.github.com/repos/sfbrigade/ballot_initiatives/contributors","created_at":"2013-06-13T02:16:06Z","description":"","forks_count":4,"homepage":null,"html_url":"https://github.com/sfbrigade/ballot_initiatives","id":10656947,"language":"JavaScript","name":"ballot_initiatives","open_issues":7,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/3926630?v=1","html_url":"https://github.com/sfbrigade","login":"sfbrigade","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2013-07-18T02:45:12Z","updated_at":"2013-07-18T02:45:18Z","watchers_count":1},"id":108,"last_updated":"Thu, 18 Jul 2013 02:45:18 GMT","last_updated_issues":"4553d9e6d2b787234fbf1a2eff34b1ba","link_url":null,"name":"ballot_initiatives","organization_name":"Code for San Francisco","type":null},"title":"Write some tests"},{"api_url":"http://codeforamerica.org/api/issues/82","body":"Get the site up on a heroku account. ","html_url":"https://github.com/sfbrigade/ballot_initiatives/issues/6","id":82,"labels":[{"color":"84b6eb","name":"enhancement","url":"https://api.github.com/repos/sfbrigade/ballot_initiatives/labels/enhancement"}],"project":{"api_url":"http://codeforamerica.org/api/projects/108","categories":null,"code_url":"https://github.com/sfbrigade/ballot_initiatives","description":"","github_details":{"contributors":[{"avatar_url":"https://avatars.githubusercontent.com/u/613334?v=1","contributions":16,"html_url":"https://github.com/andyhull","login":"andyhull","owner":false,"url":"https://api.github.com/users/andyhull"},{"avatar_url":"https://avatars.githubusercontent.com/u/1056580?v=1","contributions":10,"html_url":"https://github.com/mluedke2","login":"mluedke2","owner":false,"url":"https://api.github.com/users/mluedke2"},{"avatar_url":"https://avatars.githubusercontent.com/u/1231630?v=1","contributions":4,"html_url":"https://github.com/seanknox","login":"seanknox","owner":false,"url":"https://api.github.com/users/seanknox"},{"avatar_url":"https://avatars.githubusercontent.com/u/534176?v=1","contributions":3,"html_url":"https://github.com/jasonlally","login":"jasonlally","owner":false,"url":"https://api.github.com/users/jasonlally"},{"avatar_url":"https://avatars.githubusercontent.com/u/930705?v=1","contributions":1,"html_url":"https://github.com/charliemoseley","login":"charliemoseley","owner":false,"url":"https://api.github.com/users/charliemoseley"},{"avatar_url":"https://avatars.githubusercontent.com/u/1310178?v=1","contributions":1,"html_url":"https://github.com/julianeon","login":"julianeon","owner":false,"url":"https://api.github.com/users/julianeon"},{"avatar_url":"https://avatars.githubusercontent.com/u/567099?v=1","contributions":1,"html_url":"https://github.com/nmu","login":"nmu","owner":false,"url":"https://api.github.com/users/nmu"}],"contributors_url":"https://api.github.com/repos/sfbrigade/ballot_initiatives/contributors","created_at":"2013-06-13T02:16:06Z","description":"","forks_count":4,"homepage":null,"html_url":"https://github.com/sfbrigade/ballot_initiatives","id":10656947,"language":"JavaScript","name":"ballot_initiatives","open_issues":7,"owner":{"avatar_url":"https://avatars.githubusercontent.com/u/3926630?v=1","html_url":"https://github.com/sfbrigade","login":"sfbrigade","type":"Organization"},"participation":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"pushed_at":"2013-07-18T02:45:12Z","updated_at":"2013-07-18T02:45:18Z","watchers_count":1},"id":108,"last_updated":"Thu, 18 Jul 2013 02:45:18 GMT","last_updated_issues":"4553d9e6d2b787234fbf1a2eff34b1ba","link_url":null,"name":"ballot_initiatives","organization_name":"Code for San Francisco","type":null},"title":"Add an instance on heroku"}],"pages":{"last":"http://codeforamerica.org/api/organizations/Code for San Francisco/issues/labels/enhancement,hack?page=7&per_page=2","next":"http://codeforamerica.org/api/organizations/Code for San Francisco/issues/labels/enhancement,hack?page=2&per_page=2"},"total":14} ''')

  def test_get_organization_names(self):
    with HTTMock(self.response_content):
      response = self.client.get('/')
      self.assertEquals(self.get_context_variable('organization_names'), ['Code for South Africa', 'Open Nebraska'])

  def test_empty_widget(self):
    response = self.client.get('/widget')
    self.assert_200(response)
    self.assertEquals(self.get_context_variable('org_name'), None)
    self.assertEquals(self.get_context_variable('default_labels'), None)

    response = self.client.get('/widget?organization_name=Code+for+San+Francisco')
    self.assert_200(response)
    self.assertEquals(self.get_context_variable('org_name'), "Code for San Francisco")
    self.assertEquals(self.get_context_variable('default_labels'), None)

    response = self.client.get('/widget?default_labels=hack,help')
    self.assert_200(response)
    self.assertEquals(self.get_context_variable('org_name'), None)
    self.assertEquals(self.get_context_variable('default_labels'), "hack,help")

    response = self.client.get('/widget?default_labels=hack,help&organization_name=Code+for+San+Francisco')
    self.assert_200(response)
    self.assertEquals(self.get_context_variable('org_name'), "Code for San Francisco")
    self.assertEquals(self.get_context_variable('default_labels'), "hack,help")

  def test_succesful_issues_context_variables(self):
    with HTTMock(self.response_content):
      # Test with one label and no extra params
      labels = 'enhancement'

      response = self.client.post('/find', data=dict(labels=labels))
      self.assert_200(response)
      
      issues = self.get_context_variable('issues')
      # Verify we get the correct labels back
      self.assertEquals(2, len(issues))
      self.assertEquals(issues[0]['title'], 'add help facility')
      self.assertEquals(issues[1]['title'], 'help for non-service residents')

      # Verify we are correctly appending the text_color property to labels based on their color
      self.assertEquals(issues[1]['labels'][0]['text_color'], 'FFFFFF')
      self.assertEquals(issues[1]['labels'][1]['text_color'], '000000')

      # Verify other context variables remain the same
      self.assertEquals(self.get_context_variable('labels'), 'enhancement')
      self.assertEquals(self.get_context_variable('org_name'), 'None')
      self.assertEquals(self.get_context_variable('default_labels'), 'None')
    

if __name__ == '__main__':
  unittest.main()