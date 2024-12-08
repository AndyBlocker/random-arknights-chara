import requests
import json
import os
from pathlib import Path

def fetch_operator_data(api_url, output_file):
    params = {
        'action': 'cargoquery',
        'format': 'json',
        'tables': 'chara,chara_data,chara_extra_info,char_obtain',
        'join_on': 'chara._pageName=chara_data._pageName,chara._pageName=chara_extra_info._pageName,chara._pageName=char_obtain._pageName',
        'where': 'chara.charIndex>0',
        'fields': (
            'chara._pageName=干员,'
            'chara.profession=职业,'
            'chara.rarity=稀有度,'
            'chara.logo=标志,'
            'chara_extra_info.birthPlace=出身地,'
            'chara.team=团队,'
            'chara_extra_info.race=种族,'
            'chara.en=干员外文名,'
            'chara.jp=干员名jp,'
            'chara.eid=情报编号,'
            'chara_data.hp=满级生命,'
            'chara_data.atk=满级攻击,'
            'chara_data.def=满级防御,'
            'chara_data.res=满级法术抗性,'
            'chara_data.reDeploy=再部署时间,'
            'chara_data.cost=部署费用,'
            'chara_data.block=阻挡数,'
            'chara_data.atkSpeed=攻击速度,'
            'chara_extra_info.sex=性别,'
            'chara.position=位置,'
            'chara.tag=标签,'
            'char_obtain.obtainMethod=获得方式,'
            'chara_data.potential=潜能加成,'
            'chara_data.trust=信赖加成,'
            'chara_extra_info.phy=物理强度,'
            'chara_extra_info.flex=战场机动,'
            'chara_extra_info.tolerance=生理耐受,'
            'chara_extra_info.plan=战术规划,'
            'chara_extra_info.skill=战斗技巧,'
            'chara_extra_info.adapt=源石技艺适应性,'
            'chara.feature=特性,'
            'chara.charIndex=干员序号,'
            'chara.subProfession=子职业,'
            'chara.nation=国家,'
            'chara.org=组织'
        ),
        'limit': 5000
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'cargoquery' in data:
            operators = [entry['title'] for entry in data['cargoquery']]
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(operators, f, ensure_ascii=False, indent=4)
            print(f"干员数据已保存到 {output_file}")
            return operators
        else:
            print("API 响应中未找到 cargoquery 数据")
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")

if __name__ == "__main__":
    # MediaWiki API 地址
    api_url = "https://prts.wiki/api.php"
    
    # 输出的 JSON 文件名
    json_output = Path(__file__).parent.parent / "src" / "assets" / "operator_data.json"
    
    # 图片下载目录
    image_output_dir = Path(__file__).parent.parent / "public" / "img"
    
    # 获取干员数据
    operators = fetch_operator_data(api_url, json_output)