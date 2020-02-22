# 经济责任审计知识图谱

**此项目不再维护**，你可以通过[从具体案例了解知识图谱构建流程](https://mp.weixin.qq.com/s/D3K5yHfXMWReVgdGwX8Qtw)大致了解流程。项目始于 2018-02，终于 2018-05。原本计划毕业后继续整理，奈何自己的懒惰遇上了工作的繁忙，此后便没有继续整理，索性将当时的毕业论文与后期没有完成的书籍贴上来，供大家参考。

写书的计划是我还没有毕业时与电子工业出版编辑找到我希望能写一本书，因为内容中涉及到大量爬虫，而且爬目标网站是政府网站（不允许爬），加之 19 年网上时不时曝出某某程序员因爬虫而入狱的故事，出版社和我难免不会恐惧。

我做毕设时有一部分数据来源于导师，这部分数据属于涉密数据，总之就是各种因素加在一起这本书的出版计划泡汤了，[书籍](https://github.com/mengxiaoxu/economic_audit_knowledge_graph/tree/master/书籍)存放的是第一、二、三章的内容，当然前三章还有部分内容没有完成，但主体内容已经完备，是一个不错的参考。

第四章没有写，第五章主要是关于 Neo4J 数据库的相关知识，这些内容您可以通过网络博客轻松查到；第六章计划内容是该知识图谱可视化的实现，准备使用 tornado + vue 重新实现（程序中所给的不是这种实现方式），web 相关的内容你也可以在网上轻松查到，如果您花时间重新实现了 web 程序，欢迎您提交您的代码。

### 程序

存放经济责任审计知识图谱构建过程中的所有程序

### 数据

存放最终使用的数据

### 论文

我的毕业论文

### 书籍

未写完的书籍

# 说明

## 数据来源

所有实体数据来源于[互动百科](http://www.baike.com/)

关系数据分两部分，一部分是从[wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page)中直接爬的

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