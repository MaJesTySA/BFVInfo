import requests
import json
import pandas as pd

overview_url = 'https://api.tracker.gg/api/v2/bfv/standard/profile/{0}/{1}'
weapon_url = 'https://api.tracker.gg/api/v1/bfv/profile/{0}/{1}/weapons'
vehicle_url = 'https://api.tracker.gg/api/v1/bfv/profile/{0}/{1}/vehicles'


def get_detail(platform, id):
    session = requests.session()
    session.keep_alive = False
    try:
        response = requests.get(overview_url.format(platform, id))
    except requests.exceptions.ConnectionError:
        return json.loads('{"error":"500"}')
    if response.status_code == 404:
        return json.loads('{"error":"404"}')
    elif response.status_code == 400:
        return json.loads('{"error":"400"}')
    else:
        data_dict = json.loads(response.text, encoding='utf-8')
        # 调试用，避免过多请求
        # with open('data.txt', 'w') as f:
        #     f.write(response.text)
        #
        # with open('data.txt', 'r') as f:
        #     data_dict = json.loads(f.read())

        # 存放总览信息、武器信息、载具信息
        all_data_dict = {}
        # 解析总览信息
        required_data_dict = {
            'score_per_min': data_dict['data']['segments'][0]['stats']['scorePerMinute']['displayValue'],
            'kd': data_dict['data']['segments'][0]['stats']['kdRatio']['displayValue'],
            'kills': data_dict['data']['segments'][0]['stats']['kills']['displayValue'],
            'kills_per_min': data_dict['data']['segments'][0]['stats']['killsPerMinute']['displayValue'],
            'damage_per_min': data_dict['data']['segments'][0]['stats']['damagePerMinute']['displayValue'],
            'shots_accuracy': data_dict['data']['segments'][0]['stats']['shotsAccuracy']['displayValue'],
            'dog_tags': data_dict['data']['segments'][0]['stats']['dogtagsTaken']['displayValue'],
            'head_shots': data_dict['data']['segments'][0]['stats']['headshots']['displayValue'],
            'longest_hs': data_dict['data']['segments'][0]['stats']['longestHeadshot']['displayValue'],
            'heals': data_dict['data']['segments'][0]['stats']['heals']['displayValue'],
            'revives': data_dict['data']['segments'][0]['stats']['revives']['displayValue'],
            'resupplies': data_dict['data']['segments'][0]['stats']['resupplies']['displayValue'],
            'rank': data_dict['data']['segments'][0]['stats']['rank']['displayValue'],
            'time_played': data_dict['data']['segments'][0]['stats']['timePlayed']['displayValue'],
            'win_rate': data_dict['data']['segments'][0]['stats']['wlPercentage']['displayValue'],

            'assault_class_rank': data_dict['data']['segments'][9]['stats']['rank']['displayValue'],
            'assault_class_kills': data_dict['data']['segments'][9]['stats']['kills']['displayValue'],
            'assault_class_kd': data_dict['data']['segments'][9]['stats']['kdRatio']['displayValue'],
            'assault_class_score': data_dict['data']['segments'][9]['stats']['score']['displayValue'],
            'assault_class_kpm': data_dict['data']['segments'][9]['stats']['killsPerMinute']['displayValue'],
            'assault_class_spm': data_dict['data']['segments'][9]['stats']['scorePerMinute']['displayValue'],
            'assault_class_time': data_dict['data']['segments'][9]['stats']['timePlayed']['displayValue'],
            'assault_class_shots_acc': data_dict['data']['segments'][9]['stats']['shotsAccuracy']['displayValue'],

            'medic_class_rank': data_dict['data']['segments'][10]['stats']['rank']['displayValue'],
            'medic_class_kills': data_dict['data']['segments'][10]['stats']['kills']['displayValue'],
            'medic_class_kd': data_dict['data']['segments'][10]['stats']['kdRatio']['displayValue'],
            'medic_class_score': data_dict['data']['segments'][10]['stats']['score']['displayValue'],
            'medic_class_kpm': data_dict['data']['segments'][10]['stats']['killsPerMinute']['displayValue'],
            'medic_class_spm': data_dict['data']['segments'][10]['stats']['scorePerMinute']['displayValue'],
            'medic_class_time': data_dict['data']['segments'][10]['stats']['timePlayed']['displayValue'],
            'medic_class_shots_acc': data_dict['data']['segments'][10]['stats']['shotsAccuracy']['displayValue'],

            'pilot_class_kills': data_dict['data']['segments'][11]['stats']['kills']['displayValue'],
            'pilot_class_score': data_dict['data']['segments'][11]['stats']['score']['displayValue'],
            'pilot_class_kpm': data_dict['data']['segments'][11]['stats']['killsPerMinute']['displayValue'],
            'pilot_class_spm': data_dict['data']['segments'][11]['stats']['scorePerMinute']['displayValue'],
            'pilot_class_time': data_dict['data']['segments'][11]['stats']['timePlayed']['displayValue'],

            'recon_class_rank': data_dict['data']['segments'][12]['stats']['rank']['displayValue'],
            'recon_class_kills': data_dict['data']['segments'][12]['stats']['kills']['displayValue'],
            'recon_class_kd': data_dict['data']['segments'][12]['stats']['kdRatio']['displayValue'],
            'recon_class_score': data_dict['data']['segments'][12]['stats']['score']['displayValue'],
            'recon_class_kpm': data_dict['data']['segments'][12]['stats']['killsPerMinute']['displayValue'],
            'recon_class_spm': data_dict['data']['segments'][12]['stats']['scorePerMinute']['displayValue'],
            'recon_class_time': data_dict['data']['segments'][12]['stats']['timePlayed']['displayValue'],
            'recon_class_shots_acc': data_dict['data']['segments'][12]['stats']['shotsAccuracy']['displayValue'],

            'support_class_rank': data_dict['data']['segments'][13]['stats']['rank']['displayValue'],
            'support_class_kills': data_dict['data']['segments'][13]['stats']['kills']['displayValue'],
            'support_class_kd': data_dict['data']['segments'][13]['stats']['kdRatio']['displayValue'],
            'support_class_score': data_dict['data']['segments'][13]['stats']['score']['displayValue'],
            'support_class_kpm': data_dict['data']['segments'][13]['stats']['killsPerMinute']['displayValue'],
            'support_class_spm': data_dict['data']['segments'][13]['stats']['scorePerMinute']['displayValue'],
            'support_class_time': data_dict['data']['segments'][13]['stats']['timePlayed']['displayValue'],
            'support_class_shots_acc': data_dict['data']['segments'][13]['stats']['shotsAccuracy']['displayValue'],

            'tank_class_kills': data_dict['data']['segments'][14]['stats']['kills']['displayValue'],
            'tank_class_score': data_dict['data']['segments'][14]['stats']['score']['displayValue'],
            'tank_class_kpm': data_dict['data']['segments'][14]['stats']['killsPerMinute']['displayValue'],
            'tank_class_spm': data_dict['data']['segments'][14]['stats']['scorePerMinute']['displayValue'],
            'tank_class_time': data_dict['data']['segments'][14]['stats']['timePlayed']['displayValue'],
        }

        all_data_dict['overview'] = required_data_dict
        all_data_dict['weapons'] = get_weapons(platform, id)
        all_data_dict['vehicles'] = get_vehicles(platform, id)

        return json.dumps(all_data_dict)


def get_weapons(platform, id):
    res = requests.get(weapon_url.format(platform, id))
    data_dict = json.loads(res.text)
    # 调试用，避免过多请求
    # with open('weapon_data.txt', 'w', encoding='utf-8') as f:
    #      f.write(res.text)
    # with open('weapon_data.txt', 'r') as f:
    #     data_dict = json.loads(f.read())
    weapons_df = pd.DataFrame(columns=('type', 'name', 'kills', 'kpm', 'time', 'accuracy', 'hs'))
    for weapon in data_dict['data']['children']:
        tmp_dict = {
            'type': weapon['metadata']['categoryName'],
            'name': weapon['metadata']['name'],
            'kills': weapon['stats'][0]['displayValue'],
            'kpm': weapon['stats'][1]['displayValue'],
            'time': weapon['stats'][2]['displayValue'],
            'accuracy': weapon['stats'][5]['displayValue'],
            'hs': weapon['stats'][6]['displayValue'],
        }
        weapons_df = weapons_df.append(tmp_dict, ignore_index=True)
    i = 0
    for value in weapons_df['kills'].values:
        weapons_df['kills'].values[i] = int(value.replace(',', ''))
        i += 1
    sorted_weapons_df = weapons_df.sort_values(by='kills', ascending=False)
    return sorted_weapons_df[:20].values.tolist()


def get_vehicles(platform, id):
    res = requests.get(vehicle_url.format(platform, id))
    data_dict = json.loads(res.text)
    # with open('vehicle_data.txt', 'w', encoding='utf-8') as f:
    #      f.write(res.text)
    # with open('vehicle_data.txt', 'r') as f:
    #     data_dict = json.loads(f.read())
    vehicles_df = pd.DataFrame(columns=('type', 'name', 'kills', 'kpm', 'time'))
    for vehicle in data_dict['data']['children']:
        tmp_dict = {
            'type': vehicle['metadata']['categoryName'],
            'name': vehicle['metadata']['name'],
            'kills': vehicle['stats'][0]['displayValue'],
            'kpm': vehicle['stats'][1]['displayValue'],
            'time': vehicle['stats'][2]['displayValue'],
        }
        vehicles_df = vehicles_df.append(tmp_dict, ignore_index=True)
    i = 0
    for value in vehicles_df['kills'].values:
        vehicles_df['kills'].values[i] = int(value.replace(',', ''))
        i += 1
    sorted_vehicles_df = vehicles_df.sort_values(by='kills', ascending=False)
    return sorted_vehicles_df[:20].values.tolist()


if __name__ == '__main__':
    print(get_detail('origin', 'TULANGTV'))
