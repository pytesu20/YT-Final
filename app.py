# Input multiline YT_URLs and will output HD resolution thumbnail in a new tab in firefox

def openurl(final_url):
  import webbrowser
  webbrowser.get('firefox').open_new_tab(final_url)

print("enter multiline input: ")
#multiline inputs from user
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

print('this is the old database: ')
print(lines)

lines = [s.replace("https://www.youtube.com/watch?v=", '') for s in lines]

print('this is the new database: ')
print(lines)

list = lines

st = 'https://img.youtube.com/vi/'
end = '/maxresdefault.jpg'

result = []
for vid_id in list:
    result.append((st + vid_id + end))

print(result)
print('--------')

for eachurl in result:
  openurl(eachurl)

