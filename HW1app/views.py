from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def homepage(request):
    html = '''
    <h1> My very first Django site</h1>
    <p>Nothing much to say about this site</p>
    <a href='/hw1/about-me/'> About me </a>
    '''
    logger.info('You accessed homepage')
    return HttpResponse(html)

def about_me(request):
    html = '''
    <h1>This page about me</h1>
    <p>I am the GeekBrains student, and i study Django right now.</p>
    <a href='/hw1/homepage/'> Go back to homepage</a>'''
    logger.info('You accessed About me page')
    return HttpResponse(html)
