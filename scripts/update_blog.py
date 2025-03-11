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

# 🔹 GitHub Actions에서 실행될 때 사용자 정보 설정
with repo.config_writer() as config:
    config.set_value("user", "name", "github-actions[bot]")
    config.set_value("user", "email", "github-actions[bot]@users.noreply.github.com")

# 🔹 VELOG RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 🔹 최대 파일명 길이 제한
max_length = 30  # 너무 긴 제목 방지 (30자 제한)

# 🔹 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 1️⃣ 제목 가져오기 (한글 유지, 특수문자 제거)
    raw_title = entry.title
    safe_title = re.sub(r'[\\/*?:"<>|]', '', raw_title[:max_length])  # 파일명에 사용할 수 없는 문자 제거

    # 2️⃣ 파일 이름 설정 (한글 제목 유지)
    file_name = f"{safe_title}.md"
    file_path = os.path.join(posts_dir, file_name)

    # 3️⃣ 기존 파일 여부 확인 (있으면 수정, 없으면 새로 추가)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            old_content = file.read()

        # 기존 내용과 다를 경우 업데이트
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
print("✅ Velog posts successfully backed up to GitHub!")
