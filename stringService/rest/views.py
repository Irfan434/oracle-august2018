from django.shortcuts import render
from django.http import HttpResponse
from .utils import strUtils

# Create your views here.

def stringClean(request, iStr=''):
	return HttpResponse(strUtils.stringClean(iStr))

def maxBlock(request, iStr=''):
	return HttpResponse(strUtils.maxBlock(iStr))

def reorderBlock(request, iStr=''):
	return HttpResponse(strUtils.reorderBlock(iStr))
