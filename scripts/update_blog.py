import feedparser
import git
import os
import re

# 🔹 VELOG RSS 피드 URL (본인 벨로그 계정에 맞게 수정!)
rss_url = 'https://api.velog.io/rss/@kunhee'

# 🔹 GitHub 레포지토리 경로
repo_path = '.'

# 🔹 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 🔹 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 🔹 Git 레포지토리 로드
repo = git.Repo(repo_path)

# 🔹 VELOG RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 🔹 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 1️⃣ 글 ID 가져오기 (URL에서 추출)
    post_id = entry.link.split('/')[-1]  # 글의 고유 ID (예: 'abcdefg123456')

    # 2️⃣ 파일 이름: "ID.md" 형태로 저장 (제목이 바뀌어도 같은 파일 유지)
    file_name = f"{post_id}.md"
    file_path = os.path.join(posts_dir, file_name)

    # 3️⃣ 기존 파일 여부 확인 (있으면 수정, 없으면 새로 추가)
    if os.path.exists(file_path):
        # 파일이 존재하면, 기존 내용과 비교 후 수정
        with open(file_path, 'r', encoding='utf-8') as file:
            old_content = file.read()

        # 변경 사항이 있는 경우에만 업데이트
        if old_content != entry.description:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(entry.description)
            
            repo.git.add(file_path)
            repo.git.commit('-m', f'Update post: {entry.title}')
    
    else:
        # 새로운 글이면 새 파일 생성
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)
        
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# 🔹 변경 사항을 GitHub에 푸시
repo.git.push()
