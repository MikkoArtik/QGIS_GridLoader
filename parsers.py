

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex


def readClrFile(file_path):
    f = open(file_path,'r')
    i=0
    data = list()
    for line in f:
        i+=1
        line = line.strip()
        line = " ".join(line.split())
        if i>1:
            t = line.split()
            percent = float(t[0])
            r_value = int(t[1])
            g_value = int(t[2])
            b_value = int(t[3])
            hex_value = rgb2hex(r_value, g_value, b_value)
            data.append((percent,hex_value))
    f.close()
    return data

def recalcScale(clr_data, min_value, max_value):
    output_data=list()
    for percent, hex_value in clr_data:
        z_value = min_value +(max_value-min_value)*percent/100
        output_data.append((z_value, hex_value, str(z_value)))
    return output_data
