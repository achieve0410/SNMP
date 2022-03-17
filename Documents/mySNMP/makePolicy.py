
import pandas as pd

xls_source = pd.read_excel('excel_file.xlsx')

idx_array = []
policyNum_array = []
desc_array = []
action_array = []
enable_array = []
hit1_array = []
hit7_array = []
hit30_array = []
hit60_array = []
hit90_array = []


# print(xls_source.loc[0])
# print(xls_source['SRC'])
## print(type(xls_source['PRIORITY'][1])) -- type: float
# print(len(xls_source['SRC']))

idx, tmp = 0, 0
file_length = len(xls_source['SRC'])


## calc length of each policy
for i in range(file_length):
    if str(xls_source['PRIORITY'][i]) != 'nan':
        idx = i
        idx_array.append(idx)
    else:
        tmp+=1

# print(idx_array)
# print(len(idx_array))



## define arrays
srcName_array = [[] for _ in range(len(idx_array))]
srcAddr_array = [[] for _ in range(len(idx_array))]
dstName_array = [[] for _ in range(len(idx_array))]
dstAddr_array = [[] for _ in range(len(idx_array))]
svcName_array = [[] for _ in range(len(idx_array))]
svcAddr_array = [[] for _ in range(len(idx_array))]


## make src Array
idx, flg = 0, 0
for i in range(file_length):
    if idx_array[idx] == i:
        flg = idx
        srcName_array[flg].append(xls_source['SRC'][i])
        srcAddr_array[flg].append(xls_source['SRC ADDR'][i])
        idx += 1
    else:
        if str(xls_source['SRC'][i]) != 'nan':
            srcName_array[flg].append(xls_source['SRC'][i])
            srcAddr_array[flg].append(xls_source['SRC ADDR'][i])
        else:
            continue

# for i in range(len(idx_array)):
#     print(srcName_array[i])
#     print(srcAddr_array[i])

# print(len(srcName_array), len(srcAddr_array))



## make dst Array
idx, flg = 0, 0
for i in range(file_length):
    if idx_array[idx] == i:
        flg = idx
        dstName_array[flg].append(xls_source['DST'][i])
        dstAddr_array[flg].append(xls_source['DST ADDR'][i])
        idx += 1
    else:
        if str(xls_source['DST'][i]) != 'nan':
            dstName_array[flg].append(xls_source['DST'][i])
            dstAddr_array[flg].append(xls_source['DST ADDR'][i])
        else:
            continue

# for i in range(len(idx_array)):
#     print(dstName_array[i])
#     print(dstAddr_array[i])

# print(len(dstName_array), len(dstAddr_array))



## make svc Array
idx, flg = 0, 0
for i in range(file_length):
    if idx_array[idx] == i:
        flg = idx
        svcName_array[flg].append(xls_source['SVC'][i])
        svcAddr_array[flg].append(xls_source['SVC SPEC'][i])
        idx += 1
    else:
        if str(xls_source['SVC'][i]) != 'nan':
            svcName_array[flg].append(xls_source['SVC'][i])
            svcAddr_array[flg].append(xls_source['SVC SPEC'][i])
        else:
            continue

# for i in range(len(idx_array)):
#     print(svcName_array[i])
#     print(svcAddr_array[i])

# print(len(svcName_array), len(svcAddr_array))



## make policyNum Array
for idx in idx_array:
    policyNum_array.append(int(xls_source['POLICY ID'][idx]))
    desc_array.append(xls_source['DESC'][idx])
    action_array.append(xls_source['ACTION'][idx])
    enable_array.append(xls_source['ENABLED'][idx])
    hit1_array.append(int(xls_source['DALIY HIT COUNT'][idx]))
    hit7_array.append(int(xls_source['WEEKLY HIT COUNT'][idx]))
    hit30_array.append(int(xls_source['MONTHLY HIT COUNT'][idx]))
    hit60_array.append(int(xls_source['2MONTHLY HIT COUNT'][idx]))
    hit90_array.append(int(xls_source['QUARTERLY HIT COUNT'][idx]))
    


# print(policyNum_array)
# print(len(policyNum_array))

# print(desc_array)
# print(len(desc_array))

# print(action_array)
# print(len(action_array))

# print(enable_array)
# print(len(enable_array))

# print(hit1_array)
# print(len(hit1_array))

# print(hit7_array)
# print(len(hit7_array))

# print(hit30_array)
# print(len(hit30_array))

# print(hit60_array)
# print(len(hit60_array))

# print(hit90_array)
# print(len(hit90_array))


print(idx_array)
# print(srcAddr_array[5], dstAddr_array[5], svcAddr_array[5])

print(svcAddr_array)

for s_idx in range(len(svcAddr_array)):
    # print(svcAddr_array[s_idx])
    for s_jdx in range(len(svcAddr_array[s_idx])):
        print(svcAddr_array[s_idx][s_jdx]) ## type: str
        # print(type(svcAddr_array[s_idx][s_jdx]))

        ## manipulate port data
        new_port = ''

        # for p_idx in range(len(svcAddr_array[s_idx][s_jdx])):
        # new_port = ''
        
        ## tcp or udp
        if svcAddr_array[s_idx][s_jdx][0:3] == 'tcp' or svcAddr_array[s_idx][s_jdx][0:3] == 'udp' :
            if svcAddr_array[s_idx][s_jdx][-6] == '-':
                new_port = svcAddr_array[s_idx][s_jdx][0:3] + '-' + svcAddr_array[s_idx][s_jdx][-5:]
                print(new_port)
                # print(svcAddr_array[s_idx][s_jdx][-5:])
                # continue
            elif svcAddr_array[s_idx][s_jdx][-5] == '-':
                new_port = svcAddr_array[s_idx][s_jdx][0:3] + '-' + svcAddr_array[s_idx][s_jdx][-4:]
                print(new_port)
                # print(svcAddr_array[s_idx][s_jdx][-4:])
                # continue
            elif svcAddr_array[s_idx][s_jdx][-4] == '-':
                new_port = svcAddr_array[s_idx][s_jdx][0:3] + '-' + svcAddr_array[s_idx][s_jdx][-3:]
                print(new_port)
                # print(svcAddr_array[s_idx][s_jdx][-3:])
                # continue
            elif svcAddr_array[s_idx][s_jdx][-3] == '-':
                new_port = svcAddr_array[s_idx][s_jdx][0:3] + '-' + svcAddr_array[s_idx][s_jdx][-2:]
                print(new_port)
                # print(svcAddr_array[s_idx][s_jdx][-2:])
                # continue

            # print("YES")
        
        ## icmp
        elif svcAddr_array[s_idx][s_jdx][0:4] == 'icmp':
            new_port = svcAddr_array[s_idx][s_jdx]
            print(new_port)
        else:
            new_port = svcAddr_array[s_idx][s_jdx]
            print(new_port)
                
        svcAddr_array[s_idx][s_jdx] = new_port
        



## make Frame for Export Excel

output_frame = [{} for i in range(len(idx_array))]

for f_idx in range(len(idx_array)):
    output_frame[f_idx] = {
        'Policy ID' : policyNum_array[f_idx],
        'Enabled' : enable_array[f_idx],
        'Source Address' : srcAddr_array[f_idx],
        'Destination Address' : dstAddr_array[f_idx],
        'Service Port' : svcAddr_array[f_idx],
        'Action' : action_array[f_idx],
        'Description' : desc_array[f_idx]
    }

output = pd.DataFrame(output_frame)
# print(output)

output.to_excel('Export_Excel.xlsx')