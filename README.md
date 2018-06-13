# 经济责任审计知识图谱

还没有整理完，后面继续整理

[从具体案例了解知识图谱构建流程](https://mp.weixin.qq.com/s/D3K5yHfXMWReVgdGwX8Qtw)

### 程序

存放经济责任审计知识图谱构建过程中的所有程序

### 数据

存放最终使用的数据

# 说明

## 数据来源

所有实体数据来源于[互动百科](http://www.baike.com/)

关系数据分两部分，一部分是从[wikidata]中直接爬的

另一部分是使用程序抽取的事实三元组，将所有新闻数据和词条解释都进行实体关系抽取

事实三元组抽取程序传送门：[基于依存分析的实体关系抽取程序](https://github.com/mengxiaoxu/entity_relation_extraction)

## 构建流程

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/实现流程图.png)

## 效果展示

### 实体查询

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/实体查询.png)

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/实体查询结果.png)

### 关系查询

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/关系查询.png)

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/关系查询结果1.png)

![image](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/raw/master/数据/img/关系查询结果2.png)

## 使用

将```数据```文件夹中的数据导入neo4j数据库

实体信息导入程序：```https://github.com/mengxiaoxu/economic_audit_knowledge_graph/tree/master/程序/实体信息导入程序```

关系数据导入：

```
# 导入关系数据
LOAD CSV  WITH HEADERS FROM "file:///relation.csv" AS line
MATCH (entity1:Hudong{title:line.Hudong1}) , (entity2:Hudong{title:line.Hudong2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

# 添加索引
CREATE CONSTRAINT ON (c:Hudong)
ASSERT c.title IS UNIQUE
```

可以参考：[农业知识图谱说明](https://github.com/qq547276542/Agriculture_KnowledgeGraph/blob/master/README.md)

## 感谢

[汉语言处理包HanLP](https://github.com/hankcs/HanLP)

[中文文本分类](https://github.com/gaussic/text-classification-cnn-rnn)

[农业知识图谱](https://github.com/qq547276542/Agriculture_KnowledgeGraph)

[事实三元组抽取](https://github.com/twjiang/fact_triple_extraction)

[开放中文实体关系抽取](http://www.docin.com/p-1715877509.html)

[中文自然语言处理相关资料](https://github.com/mengxiaoxu/Awesome-Chinese-NLP)