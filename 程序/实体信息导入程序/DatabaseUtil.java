package com.qaweb.utils;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;

import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;
import org.neo4j.driver.v1.Session;

import net.sf.json.JSONObject;

public class DatabaseUtil {

	
	/**
	 * 
	 * @Description 数据导入neo4j
	 * @author 刘绪光
	 * @Time 2018年4月11日上午11:55:56
	 */
	public static void main(String[] args) {
		
		try {
			
			File file = new File("D:/workspace/data/互动百科数据.json");
			File writeFile = new File("D:/workspace/data/导入失败数据.json");
			
			writeFile.createNewFile();
			BufferedWriter out = new BufferedWriter(new FileWriter(writeFile));
			
			InputStreamReader reader = new InputStreamReader(new FileInputStream(file));
			BufferedReader br = new BufferedReader(reader);
			
			String line = "";
			
			line = br.readLine();
			
			int i = 0;
			
			Driver driver = GraphDatabase.driver( "bolt://localhost:7687", AuthTokens.basic( "neo4j", "root" ) );
			Session session = driver.session();
			
			while(i < 100397){
				line = br.readLine();
				
				if(line != null){
					JSONObject json = JSONObject.fromObject(line);
					// System.out.println(json);
					try{
						session.run( "CREATE (a:Hudong {title: '" + json.get("title") + "',url:'"
								+ json.get("url") + "',image:'"
								+ json.get("image") +"',openTypeList:'"
								+ json.get("openTypeList") + "',detail:'"
								+ json.get("detail") + "',baseInfoKeyList:'"
								+ json.get("baseInfoKeyList") + "',baseInfoValueList:'"
								+ json.get("baseInfoValueList") + "' })");
						/*session.run("match(n:hudong) where n.title = '"
								+ json.get("title") + "' delete n");*/
					
					}catch(Exception e){
						System.out.println(line);
						out.write(line + "\n");
						out.flush();
						System.err.println("导入失败,写入文件=======================");
					}
					i++;
					
					if(i % 50 == 0){
						System.out.println(i);
					}
				}
				
			}
			
			br.close();
			reader.close();
			out.close();
			System.out.println("导入完成=====================");
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
}
