#v5 support remote location
import os
import re
import os.path
import subprocess
import platform

#from random_word import RandomWords
#from quote import quote

print("Demi Maintenance HINCD yang lebih baik")
print("Ya Allah mudah2an hari ini ga ada issue, biar ngerjain report pm dengan tenang - Satria Adidaya")
#res = quote('Cinta',limit=1)
#print(res)
print("Lokasi File Harus Lengkap, contoh D:\OneDrive - Multipolar Technology\Maintenance\BNP Paribas Investment\\2021\Desember 2021\source")
source = input("Source File ( Folder ) : ")

file_name = os.path.join(source, "result.csv")         

#file_name = 'result.csv'

start_version_ios = 'Version'
end_version_ios = 'RELEASE SOFTWARE'
start_version_nx9k = 'NXOS: version'
end_version_nx9k = ''
start_version_nx = 'system:    version '
end_version_nx = ''
start_uptime = 'uptime is'
end_uptime = 'minute'
start_cpu = 'last 60 minutes'
end_cpu = 'last 72 hours'
start_type_ios = 'cisco'
end_type_ios = 'processor'
start_type_nx9k = 'cisco'
end_type_nx9k = 'chassis'
start_type_rtr3900 = 'Cisco'
end_type_rtr3900 = '-CHASSIS'
start_type_rtr2900 = 'Cisco'
end_type_rtr2900 = '/K9'
start_type_nx = 'cisco'
end_type_nx = 'Chassis'
start_mem_total_ios = 'Processor Pool Total: '
end_mem_total_ios = 'Used'
start_mem_usage_ios = 'Used: '
end_mem_usage_ios = 'Free:'
start_mem_total_nx9k = 'Memory usage:   '
end_mem_total_nx9k = 'K total'
start_mem_usage_nx9k = 'total,   '
end_mem_usage_nx9k = 'K used'
start_mem_total_cat3850 = 'System memory  : '
end_mem_total_cat3850 = 'K total'
start_mem_usage_cat3850 = 'total, '
end_mem_usage_cat3850 = 'K used'
start_serial_number = 'Processor board ID '
end_serial_number = ''
start_serial_number_nx9k = '  Processor Board ID '
end_serial_number_nx9k = ''
start_system_returned_ios = 'System returned '
end_system_returned_ios = ''
start_system_restarted_ios = 'System restarted '
end_system_restarted_ios = ''
start_system_image_ios = 'System image file is '
end_system_image_ios = ''
start_last_reload_ios = 'Last reload reason:'
end_last_reload_ios = ''
start_image_file_nx = 'NXOS image file is: '
end_image_file_nx = ''
start_last_reset_nx = 'Last reset'
end_last_reset_nx = ''
start_lr_reason_nx = '  Reason:'
end_lr_reason_nx = ''

def to_doc_ios(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()

def to_doc_cat3850(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()

def to_doc_nx9k(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()    

def to_doc_nx(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()    

def to_doc_rtr2900(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()   

def to_doc_rtr3900(file_name, payload):
    f = open(file_name, 'a')
    f.write(payload)
    f.write('\n')
    f.close()   

def to_doc_w(file_name, payload):
    f = open(file_name, 'w')
    f.write('Hostname;Uptime;Max CPU;Avg CPU;Type;Version;Mem Usage;Serial Number (Processor board ID);System returned;System restarted;System image file;Last reload reason;NXOS image file;Last reset;Last reset reason')
    f.write("\n")
    f.write(payload)
    f.close()


to_doc_w(file_name, "")

def search_version_ios():
    find_version_ios = re.search(start_version_ios + '(.*)' + end_version_ios, text)
    if find_version_ios is None:
        version_ios = 'Cant find version ios'
    else:
        version_ios = find_version_ios.group(1)
    return version_ios

def search_version_nx9k():
    find_version_nx9k = re.search(start_version_nx9k + '(.*)' + end_version_nx9k, text)
    if find_version_nx9k is None:
        version_nx9k = 'Cant find version nx9k'
    else:
        version_nx9k = find_version_nx9k.group(1)
    return version_nx9k

def search_version_nx():
    find_version_nx = re.search(start_version_nx + '(.*)' + end_version_nx, text)
    if find_version_nx is None:
        version_nx = 'Cant find version nx'
    else:
        version_nx = find_version_nx.group(1)
    return version_nx

def search_type_ios():
    find_type_ios = re.search(start_type_ios + '(.*)' + end_type_ios, text)
    if find_type_ios is None:
        type_ios = 'Cant find type ios'
    else:
        type_ios = find_type_ios.group(1)
    return type_ios

def search_type_nx9k():
    find_type_nx9k = re.search(start_type_nx9k + '(.*)' + end_type_nx9k, text)
    if find_type_nx9k is None:
        type_nx9k = 'Cant find type nx9k'
    else:
        type_nx9k = find_type_nx9k.group(1)
    return type_nx9k

def search_type_nx():
    find_type_nx = re.search(start_type_nx + '(.*)' + end_type_nx, text)
    if find_type_nx is None:
        type_nx = 'Cant find type nx'
    else:
        type_nx = find_type_nx.group(1)
    return type_nx

def search_type_rtr3900():
    find_type_rtr3900 = re.search(start_type_rtr3900 + '(.*)' + end_type_rtr3900, text)
    if find_type_rtr3900 is None:
        type_rtr3900 = 'Cant find type Rtr3900'
    else:
        type_rtr3900 = find_type_rtr3900.group(1)
    return type_rtr3900

def search_type_rtr2900():
    find_type_rtr2900 = re.search(start_type_rtr2900 + '(.*)' + end_type_rtr2900, text)
    if find_type_rtr2900 is None:
        type_rtr2900 = 'Cant find type Rtr2900'
    else:
        type_rtr2900 = find_type_rtr2900.group(1)
    return type_rtr2900

def search_serial_number():
    find_serial_number = re.search(start_serial_number + '(.*)' + end_serial_number, text)
    if find_serial_number is None:
        serial_number = 'Cant find serial number'
    else:
        serial_number = find_serial_number.group(1)
    return serial_number

def search_serial_number_nx9k():
    find_serial_number_nx9k = re.search(start_serial_number_nx9k + '(.*)' + end_serial_number_nx9k, text)
    if find_serial_number_nx9k is None:
        serial_number_nx9k = 'Cant find serial number nx9k'
    else:
        serial_number_nx9k = find_serial_number_nx9k.group(1)
    return serial_number_nx9k

def search_uptime():
    find_uptime = re.search(start_uptime + '(.*)' + end_uptime, text)
    if find_uptime is None:
        uptime = 'Cant find uptime'
    else:
        uptime = find_uptime.group(1)
    return uptime    

def search_cpu():
    cpu_usage = []

    # finding cisco cpu history for given text file with given parameter
    find_cpu = re.search(start_cpu + '(.*?)' + end_cpu, text, re.DOTALL)

    # -------------------------FINDING MAX CPU-----------------------------

    # Convert re.search result from find_cpu to string
    # Using split to delete few first row and rsplit to delete few last row
    # split for first 2 row, rsplit for last 13 row

    if find_cpu is None:
        max_cpu = 'Cant find max CPU'
        avg = 'Cant find average CPU'
    else:
        cpu_row_max = (find_cpu.group(1).split("\n", 2)[-1]).rsplit("\n", 13)[0]

        # get row from last 2 line
        cpu_first_row = cpu_row_max.splitlines()[-2]

        # get row from last line
        cpu_second_row = cpu_row_max.splitlines()[-1]

        # make an array which element is every single character in a row
        # remove first 4 character
        arr_first_row = list(cpu_first_row[4:])
        arr_second_row = list(cpu_second_row[4:])

        # make a for loop to join 2 array above
        for i in range(0, len(arr_second_row)):
            if arr_first_row[i] == ' ':
                arr_first_row[i] = '0'
            if arr_second_row[i] == ' ':
                arr_second_row[i] = '0'
            arr_join = arr_first_row[i] + arr_second_row[i]
            cpu_usage.append(arr_join)

        # convert cpu_usage array to int to get max value of its element
        # then return it to string again to write the result
        max_cpu = str(max(map(int, cpu_usage)))

        # -------------------------FINDING CPU AVERAGE-----------------------------

        # split for first 2 row
        # rsplit for last 3 row
        # make an array from last 10 row

        cpu_row_avg = ((find_cpu.group(1).split("\n", 2)[-1]).rsplit("\n", 3)[0]).splitlines()[-10:]

        # check for # in every element of the cpu_row_avg
        avg_raw = [i for i in cpu_row_avg if '#' in i]

        # if there is no # in array, then it must be below 10% average
        if len(avg_raw) == 0:
            avg = '<10%'

        # else get first element of array because it must be highest
        # remove any non numerical character
        else:
            avg = re.sub("[^0-9]", "", avg_raw[0])

    return max_cpu, avg

def search_mem_total_ios():
    find_mem_total_ios = re.search(start_mem_total_ios + '(.*)' + end_mem_total_ios, text)
    if find_mem_total_ios is None:
        mem_total_ios = 'Cant find mem total ios'
    else:
        mem_total_ios = find_mem_total_ios.group(1)
    return mem_total_ios

def search_mem_usage_ios():
    find_mem_usage_ios = re.search(start_mem_usage_ios + '(.*)' + end_mem_usage_ios, text)
    if find_mem_usage_ios is None:
        mem_usage_ios = 'Cant find mem usage ios'
    else:
        mem_usage_ios = find_mem_usage_ios.group(1)
    return mem_usage_ios

def search_mem_total_nx9k():
    find_mem_total_nx9k = re.search(start_mem_total_nx9k + '(.*)' + end_mem_total_nx9k, text)
    if find_mem_total_nx9k is None:
        mem_total_nx9k = 'Cant find mem total nx'
    else:
        mem_total_nx9k = find_mem_total_nx9k.group(1)
    return mem_total_nx9k

def search_mem_usage_nx9k():
    find_mem_usage_nx9k = re.search(start_mem_usage_nx9k + '(.*)' + end_mem_usage_nx9k, text)
    if find_mem_usage_nx9k is None:
        mem_usage_nx9k = 'Cant find mem usage nx'
    else:
        mem_usage_nx9k = find_mem_usage_nx9k.group(1)
    return mem_usage_nx9k

def search_mem_total_cat3850():
    find_mem_total_cat3850 = re.search(start_mem_total_cat3850 + '(.*)' + end_mem_total_cat3850, text)
    if find_mem_total_cat3850 is None:
        mem_total_cat3850 = 'Cant find mem total cat3850'
    else:
        mem_total_cat3850 = find_mem_total_cat3850.group(1)
    return mem_total_cat3850

def search_mem_usage_cat3850():
    find_mem_usage_cat3850 = re.search(start_mem_usage_cat3850 + '(.*)' + end_mem_usage_cat3850, text)
    if find_mem_usage_cat3850 is None:
        mem_usage_cat3850 = 'Cant find mem usage cat3850'
    else:
        mem_usage_cat3850 = find_mem_usage_cat3850.group(1)
    return mem_usage_cat3850

def search_system_returned_ios():
    find_system_returned_ios = re.search(start_system_returned_ios + '(.*)' + end_system_returned_ios, text)
    if find_system_returned_ios is None:
        system_returned_ios = 'Cant find system returned ios'
    else:
        system_returned_ios = find_system_returned_ios.group(1)
    return system_returned_ios

def search_system_restarted_ios():
    find_system_restarted_ios = re.search(start_system_restarted_ios + '(.*)' + end_system_restarted_ios, text)
    if find_system_restarted_ios is None:
        system_restarted_ios = 'Cant find system restarted ios'
    else:
        system_restarted_ios = find_system_restarted_ios.group(1)
    return system_restarted_ios

def search_system_image_ios():
    find_system_image_ios = re.search(start_system_image_ios + '(.*)' + end_system_image_ios, text)
    if find_system_image_ios is None:
        system_image_ios = 'Cant find system image ios'
    else:
        system_image_ios = find_system_image_ios.group(1)
    return system_image_ios

def search_last_reload_ios():
    find_last_reload_ios = re.search(start_last_reload_ios + '(.*)' + end_last_reload_ios, text)
    if find_last_reload_ios is None:
        last_reload_ios = 'Cant find last reload'
    else:
        last_reload_ios = find_last_reload_ios.group(1)
    return last_reload_ios

def search_image_file_nx():
    find_image_file_nx = re.search(start_image_file_nx + '(.*)' + end_image_file_nx, text)
    if find_image_file_nx is None:
        image_file_nx = 'Cant find system returned ios'
    else:
        image_file_nx = find_image_file_nx.group(1)
    return image_file_nx

def search_last_reset_nx():
    find_last_reset_nx = re.search(start_last_reset_nx + '(.*)' + end_last_reset_nx, text)
    if find_last_reset_nx is None:
        last_reset_nx = 'Cant find system restarted ios'
    else:
        last_reset_nx = find_last_reset_nx.group(1)
    return last_reset_nx

def search_lr_reason_nx():
    find_lr_reason_nx = re.search(start_lr_reason_nx + '(.*)' + end_lr_reason_nx, text)
    if find_lr_reason_nx is None:
        lr_reason_nx = 'Cant find system image ios'
    else:
        lr_reason_nx = find_lr_reason_nx.group(1)
    return lr_reason_nx



your_path = source
files = os.listdir(your_path)
for file in files:
    if os.path.isfile(os.path.join(your_path, file)) and file.endswith('.txt'):
        f = open(os.path.join(your_path, file ),'r')
        text = f.read()
        
        print("Processing " + file + " .......")

        hostname = os.path.splitext(file)[0]        
        version_output_ios = search_version_ios()
        version_output_nx9k = search_version_nx9k()
        version_output_nx = search_version_nx()
        type_output_ios = search_type_ios()
        type_output_nx9k = search_type_nx9k()
        type_output_nx = search_type_nx()
        type_output_rtr3900 = search_type_rtr3900()
        type_output_rtr2900 = search_type_rtr2900()
        uptime_output = search_uptime()
        cpu_output = search_cpu()
        
        mem_total_ios_output = search_mem_total_ios()
        mem_usage_ios_output = search_mem_usage_ios()

        mem_total_nx9k_output = search_mem_total_nx9k()
        mem_usage_nx9k_output = search_mem_usage_nx9k()

        mem_total_cat3850_output = search_mem_total_cat3850()
        mem_usage_cat3850_output = search_mem_usage_cat3850()

        sn_output = search_serial_number()
        sn_nx9k_output = search_serial_number_nx9k()

        returned_ios_output = search_system_returned_ios()
        restarted_ios_output = search_system_restarted_ios()
        image_ios_output = search_system_image_ios()
        reload_ios_output = search_last_reload_ios()

        image_nx_output = search_image_file_nx()
        last_reset_nx_output = search_last_reset_nx()
        lr_reason_nx_output = search_lr_reason_nx()

        if version_output_ios != 'Cant find version ios' and type_output_ios != 'Cant find type ios' and mem_total_ios_output != 'Cant find mem total ios' and sn_output != 'Cant find serial number':
            results_ios = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_ios + ';' + version_output_ios + ';' + '=' + mem_usage_ios_output + '/' + mem_total_ios_output + '*100;' + sn_output + ';System returned ' + returned_ios_output + ';System restarted ' + restarted_ios_output + ';System image file is ' + image_ios_output + ';Last reload reason: ' + reload_ios_output + ';NXOS Only' + ';NXOS Only' + ';NXOS Only'
            to_doc_ios(file_name, results_ios)
        #    print(results_ios)
        elif version_output_nx9k != 'Cant find version nx9k' or type_output_nx9k != 'Cant find type nx9k':
            results_nx9k = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_nx9k + ';' + version_output_nx9k + ';' + '=' + mem_usage_nx9k_output + '/' + mem_total_nx9k_output + '*100;' + sn_nx9k_output + ';IOS Only' + ';IOS Only' + ';IOS Only' + ';IOS Only; NXOS image file is: ' + image_nx_output + ';Last reset' + last_reset_nx_output + ';Last reset reason:' + lr_reason_nx_output
            to_doc_nx9k(file_name, results_nx9k)
        #    print(results_nx9k)
        elif version_output_ios != 'Cant find version ios' and type_output_ios != 'Cant find type ios' or type_output_rtr3900 != 'Cant find type Rtr3900' and mem_total_cat3850_output != 'Cant find mem total cat3850' and mem_usage_cat3850_output != 'Cant find mem total cat3850':
            results_cat3850 = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_ios + ';' + version_output_ios + ';' + '=' + mem_usage_cat3850_output + '/' + mem_total_cat3850_output + '*100;' + sn_output + ';System returned ' + returned_ios_output + ';System restarted ' + restarted_ios_output + ';System image file is ' + image_ios_output + ';Last reload reason: ' + reload_ios_output + ';NXOS Only' + ';NXOS Only' + ';NXOS Only'
            to_doc_cat3850(file_name, results_cat3850)
        #    print(results_cat3850)
        elif version_output_nx != 'Cant find version nx' and type_output_nx != 'Cant find type nx':
            results_nx = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_nx + ';' + version_output_nx + ';' + '=' + mem_usage_nx9k_output + '/' + mem_total_nx9k_output + '*100;' + sn_nx9k_output + ';IOS Only' + ';IOS Only' + ';IOS Only' + ';IOS Only; NXOS image file is: ' + image_nx_output + ';Last reset' + last_reset_nx_output + ';Last reset reason:' + lr_reason_nx_output
            to_doc_nx(file_name, results_nx)
        #    print(results_nx)
        elif type_output_rtr3900 != 'Cant find type Rtr3900':
            results_rtr3900 = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_rtr3900 + '-CHASSIS;' + version_output_ios + ';' + '=' + mem_usage_ios_output + '/' + mem_total_ios_output + '*100;' + sn_output + ';System returned ' + returned_ios_output + ';System restarted ' + restarted_ios_output + ';System image file is ' + image_ios_output + ';Last reload reason: ' + reload_ios_output + ';NXOS Only' + ';NXOS Only' + ';NXOS Only'
            to_doc_rtr3900(file_name, results_rtr3900)
        #    print(results_rtr3900)
        else:
            results_rtr2900 = hostname + ';' + uptime_output + ' minutes;' + cpu_output[0] + ';' + cpu_output[1] + ';' + type_output_rtr2900 + '/K9;' + version_output_ios + ';' + '=' + mem_usage_ios_output + '/' + mem_total_ios_output + '*100;' + sn_output + ';System returned ' + returned_ios_output + ';System restarted ' + restarted_ios_output + ';System image file is ' + image_ios_output + ';Last reload reason: ' + reload_ios_output + ';NXOS Only' + ';NXOS Only' + ';NXOS Only'
            to_doc_rtr2900(file_name, results_rtr2900)
        #    print(results_rtr2900)
        
        f.close()
print("File result.csv ada di folder " + source)
open_file = source + "\\result.csv"
os.path.normpath(open_file)
os.system("start EXCEL.EXE " + '"' + open_file +'"')
