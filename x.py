import re

# 마크다운 텍스트
markdown_text = """
Here is an image: ![alt text](images/example_image.png)
Another image: ![](assets/picture.jpg)
Here is another format: ![[images/sample_image.jpg]]
"""

# 두 가지 형식을 모두 처리하는 정규식 패턴
pattern = r'!\[.*?\]\((.*?)\)|!\[\[(.*?)\]\]'

# 교체 함수 정의
def format_and_add_resource_prefix(match):
    # 일반적인 형식 ![ ]( )인 경우
    if match.group(1):
        return f'![{match.group(0)[2:-len(match.group(1)) - 3]}](resource/{match.group(1)})'
    # ![[ ]] 형식인 경우 이를 ![ ]( )로 변환하고 resource/ 추가
    else:
        return f'![]({ "resource/" + match.group(2) })'

# re.sub로 매칭된 문자열 앞에 'resource/' 삽입 및 ![[ ]] 형식 변환
modified_text = re.sub(pattern, format_and_add_resource_prefix, markdown_text)

# 결과 출력
print(modified_text)

