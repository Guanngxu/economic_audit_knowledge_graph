# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
 
import sys
sys.path.append("..")
from toolkit.pre_load import pre_load_thu,neo_con,predict_labels
from toolkit.NER import get_NE,temporaryok,get_explain,get_detail_explain

# 读取实体解析的文本
def ER_post(request):
	ctx = {}

	#根据传入的实体名称搜索出关系
	if(request.GET):
		entity = request.GET['title']
		res = None
		#连接数据库
		db = neo_con
		entityRelation = db.getEntityRelationbyEntity(entity)
		if len(entityRelation) == 0:
			res = "false"
			#若数据库中无法找到该实体，则返回数据库中无该实体
		else:
			res = "true"
			#返回查询结果
			return HttpResponse(res)

	return HttpResponse(res)
	
