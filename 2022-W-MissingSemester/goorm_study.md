# Shell & Shell Editors

## 1. 컴퓨터의 기본적인 시스템 체계(운영체제)

### **기본적인 컴퓨터 체계**

컴퓨터는 하드웨어와 소프트웨어로 나뉘고, 소프트웨어는 시스템 소프트웨어와 응용 소프트웨어로 나뉜다. 시스템 소프트웨어는 사용자들이 컴퓨터에서 응용 소프트웨어를 실행시키려 할 때 하드웨어와의 소통을 통해 수행시켜주는 프로그램들의 집합이다. 우리는 이 프로그램의 집합체를 운영체제라고 한다. 

### **운영체제의 기본적인 구조**

프로그램들을 실행시킬 때 공통적으로 내재되어야 하는 프로그램들을 운영체제라고 한다.

> 예를 들어, A(B + C) = AB + AC 와 같은 경우, A를 컴퓨터에 내장시켜두고 B와 C만 입력받아 원하는 값을 구하는 것
> 

운영체제가 컴퓨터에서 차지하는 공간은 하드웨어와의 소통을 주관하는 커널 공간과 사용자와 직접적으로 연결된 사용자 공간으로 분류된다. 

### **시스템 체계의 구조**

Shell은 커널공간과 사용자공간을 이어주는 공간 역할을 한다. 사용자 공간에서 커널 공간으로 내리는 명령어를 Shell이라고 한다. 명령어를 입력하는 공간이 우리에게 어떻게 보여질까? CLI와 GUI의 개념은 여기서 나온다. 

CLI는 Command Line Interface로 명령어를 치는 공간이다. window+r → cmd enter 하면 나오는 까만 창은 윈도우에서 사용하는 커맨드 프롬포트라는 하나의 커맨드 실행 창이다. window+r → powershell enter 하면 나오는 파란 창은 파워 쉘이다. 윈도우는 이와 같이 커맨드 프롬포트와 파워 쉘, 이 두 가지로 커널 공간과 이야기할 수 있는 공간이 마련되어있다.  GUI는 Graphical User Interface로 바탕화면 같은 것이 그 예이다. 마우스 사용으로 제어한다. 서버 개발 등을 할 때에는 GUI 환경에서 작업하는 것은 힘들다. 기본적인 명령어만 익혀도 컴퓨터 설정을 할 때 CLI 환경으로 자유롭게 할 수 있을 것이다.

### **핵심 내용**

Shell은 운영체제 중 사용자와 닿아 있는 사용자 공간과 하드웨어와 밀접한 커널 공간을 이어주는 역할을 하는 공간이다. 명령어를 입력하는 공간은 CLI(까만창, 마우스X), GUI(바탕화면 등, 마우스 O) 이 두 가지 모습으로 우리에게 보여지는 CLI 환경에서 명령어를 사용해 제어하는 것이 서버 개발 등을 할 때는 더 편하다.

## 2. Shell 커맨드 명령어

### **Shell 실습을 위한 환경구축**

운영체제의 종류가 바뀐다면 구성된 공간의 성격과 명령어가 달라질 것이다. 우리가 자주 볼 수 있는 운영 체제는 Window, 맥OS, Linux 세 가지가 있다. 우리는 이번 수업에서 Linux 운영체제의 Shell 명령어와 Window의 파워 쉘에 대해 알아볼 것이다. Linux 운영 체제 실습을 위해서는 먼저 환경을 설정해야 한다. (+ CLI 창에서는 왼쪽 마우스로 드래그하면 클립보드에 복사되고 오른쪽 마우스를 클릭하면 붙여넣기가 된다) → ubuntu 설치.

+) 컴퓨터에는 하나의 운영체제만 깔린다. wsl은 윈도우 환경에서 리눅스를 사용할 수 있도록 만들어주는 리눅스용 윈도우 하위 시스템이다. 우리는 윈도우 운영체제의 폴더들을 똑같이 접근할 수 있다. 

### **기본적인 Shell 명령어**

- `pwd` (Print working directory) : 현재 작업중인 디렉터리 출력
- `cd` (Change Directory) : 디렉터리 (경로) 이동 (하위 디렉터리로)
- `cd ..` : (상위 디렉터리로)
- `ls` (List) : 디렉터리 목록 확인
- `cp` (Copy) : 파일 또는 디렉터리 복사 (cp jay.txt jay2.txt) (cp jay2.txt /mnt/d)
- `mv` (Move) : 파일 혹은 디렉터리의 이동
- `mkdir` (Make Directory) : 디렉터리의 생성
- `rm` (Remove)  : 파일이나 디렉터리를 지움
- `rm -d` : 빈 디렉터리를 지움
- `cat` (concatenate) : 1) 단순 파일 내용 출력 2) 파일의 조작 (단순히 `cat` 만 사용하면 문서를 읽는 역할을 하지만 `cat >` 을 하면 파일 안에 문장을 입력시키거나 지울 수 있다.)
- `--help` : 명령어 사용 방법 알려줌  `cp --help`
- `man` (Manual) : 명령어의 역할, 사용법, 옵션을 설명해줌, q 치면 설명 사라짐
- Find 명령어나 파이프라인, Grep 명령어 같은 경우에는 간단하게 설명하기 힘들어 과제로 구글로 서치해보세요
- Find 명령어 : 찾을 때
- 파이프라인 : 앞 명령어 수행의 결과를 받아 다음 명령어 수행
- Grep 명령어 : 입력으로 전달된 파일 내 지정 문자열 찾아 출력

### **Shell 실습을 위한 환경구축**

Window 운영체제에서 Power Shell을 다룰 건데 cmd도 존재한다. 하지만 Power Shell 환경이 개발자들에게 더 선호된다. Power Shell 에서는 Linux 명령어들을 등록시켜 그대로 사용할 수 있고 이것이 Power Shell 의 강점 중 하나이다.

PowerShell의 세 가지 주요 Cmdlet

- Get-Command : 현재 컴퓨터에 사용 가능한 명령어를 검색하고 싶을 때
- Get-Help : 명령어를 어떻게 사용하는지 알아볼 때 (-detailed)명령을 통해 옵션 확인도 가능
- Get-Member : 개체 유형의 정식 이름과 멤버의 목록을 보고싶을 때

Alias를 활용하면 첫 시작이 쉽다.

파이프라인의 사용을 매우 추천합니다.

자동화 스크립트 .sh를 작성하는 것에 유용하다.

## 3. vi를 사용한 문서편집 (Shell Editor)

### **리눅스 상에서의 문서 편집기의 종류 및 특징**

GUI 환경과 달리 리눅스에서는 터미널에서 직접적으로 사용할 수 있는 편집기인 vi를 통해서 문서를 편집할 수 있다.

### **기본 사용 방법**

마지막 행 모드, 명령 모드, 입력 모드가 존재한다. 

**명령 모드** : 커서 이동 / 줄, 글자 삭제, 복사

- `zz` : 작업한 내용을 저장하고 vi를 종료
- `i` : 현재 커서 자리에 입력 (입력 모드로 전환)
- `a` : 현재 커서 다음 자리에 입력 (입력 모드로 전환)
- `:` : 마지막 행 모드로 전환

**입력 모드** : 문자의 입력

문자의 입력이 가능하고, ESC를 눌러 명령 모드로 이동할 수 있습니다

**마지막행 모드** :  저장 및 종료

명령 모드에서 `:` 를 입력하면 전환되는 모드이며, 저장과 종료가 가능합니다

- `q` : 작업한 것이 없을 시 종료
- `q!` : 작업한 내용을 저장하지 않고 종료
- `w (파일명)` : 현재 작업한 내용을 저장만 함, 파일명을 입력 시 다른 이름으로 저장
- `wq` : 작업한 내용을 저장하고 종료
- `wq!` : 작업한 내용을 저장한 뒤 강제로 종료

### **추가 기능**

**커서 이동하기**

vi에서는 `k` (위), `l` (오른쪽), `h` (왼쪽), `j` (아래) 로 커서를 이동할 수 있다. 

**명령 취소하기**

삭제나 수정을 잘못할 경우 ctrl + z 가 아닌 u를 눌러 명령을 취소할 수 있다.

**Page Down, Page Up**

**복사, 자르기, 붙여넣기**

- `yy` : 커서가 위치한 행을 복사 (명령 앞에 숫자 입력 시 입력 숫자만큼의 행을 복사 `3yy`)
- `dd` : 커서가 위치한 행을 잘라냄 (명령 앞에 숫자 입력 시 입력 숫자만큼의 행을 잘라냄)
- `p` : 커서가 위치한 행의 아래쪽에 붙여넣음

**문자열 검색하기**

ctrl+f 가 아닌 `/문자열` 으로 아래 방향으로 찾고 `?문자열` 으로 위 방향으로 찾을 수 있다.

기존 찾던 방향으로 계속 문자열을 찾을 경우 `n`, 반대 방향으로 문자열을 찾을 경우는 `N` 

# Version Control (Git & Github)

## 1. 버전관리에 대해서

### 버전 관리가 무엇일까

버전 관리(Version Control): 파일 변화를 시간에 따라 기록하고 나중에 특정 시점의 버전을 꺼내올 수 있는 시스템

버전 관리 시스템의 종류 : Git, Subversion, Mercurial, ...

### 사용하는 이유

- 파일을 잃거나 잘못 고쳤을 때 복구하기 용이
- 어느 부분이 변경되었는지 추적
- 누가 언제 만들어낸 것인지 알기 위해 (협업 시)

### 버전 관리 종류

**로컬 버전 관리**

가장 간단하게 버전을 관리하는 방법은 디렉토리에 파일 복사하기가 있다. 하지만 파일을 잘못 복사하거나 삭제해버리면 돌이킬 수 없어 버전 관리 도구가 생겼다. VCS라는 버전 관리 도구에서는 로컬에서 데이터베이스를 이용해서 파일의 변경 정보를 관리하고 있다.

**중앙집중식 버전 관리**

파일 관리는 중앙 서버에서 하고 개발자들은 중앙 서버에서 파일들을 다운받아 사용하는 방법. 하지만 모든 파일이 중앙 서버에 있기 때문에 서버에 문제가 발생하면 로컬에서 작업하는 개발자들은 문제가 해결되기 전까지 협업을 할 수 없다.

**분산 버전 관리**

로컬과 서버에 저장소가 모두 존재한다. 서버에 있는 저장소를그대로 로컬에 복제해서 사용하므로 서버에 문제가 발생하면 로컬 저장소를 그대로 올려 작업을 진행할 수 있다.

### git

**git이란?**

오픈 소스로 관리되는 분산 버전 관리 시스템이다. 2005년 BitKeeper의 유료화로 개발된 도구로, 리누스 토발즈가 리눅스 개발을 위해 만든 버전 관리 도구이다.

**장점**

- 빠른 속도
- 단순한 구조
- 동시 다발적으로 개발
- 완벽한 분산으로 서버 측의 저장소와 개발자들의 환경에 저장소가 존재해 저장소 한 곳에서 복제를 하면 다시 작업이 가능함
- 대형 프로젝트에서도 속도 원활 (성능이 우수)

## 2. git 입문하기

### 로컬 저장소 만들기

- `$ git config --global init.defaultBranch main` : 기본 브랜치의 이름을 main으로 설정. 작년까지 git의 기본 브랜치 이름은 master였지만 Black Lives Matter 이후로 main으로 변경되었다.
- `$ git init` : git 저장소 생성하기 - 자신이 원하는 디렉터리 위치로 가서 명령어 실행하면 git 저장소를 생성할 수 있다. (User 폴더 내에서 git 저장소를 만들 것을 권장)
    - Window 기준 - C:\Users\<유저이름>\hufs-missing-semester
        
        ```bash
        $ md ~/hufs-missing-semester
        $ cd ~/hufs-missing-semester
        $ git init
        ```
        
    - Linux - /home/<..>/hufs-missing-.. Mac - /Users/<..>/hufs-missing-..
        
        ```bash
        $ mkdir ~/hufs-missing-semester
        $ cd ~/hufs-missing-semester
        $ git init
        ```
        

### Add 명령 : git 저장소에 파일을 추가하는 명령어

```powershell
$ git add first.txt
$ git status
```

hufs-missing-semester 디렉터리 안에 first.txt를 생성한 뒤 `$ git add first.txt` 로 파일을 저장소에 추가하고 `$ git status` 로 추가한 파일을 확인할 수 있다.

### Commit 명령 : git에서 관리할 파일을 추가하는 명령어

**커밋**

소스 코드 일부의 최신 병경사항을 추가해 저장소의 최상위 기록으로 만드는 방법

```powershell
$ git commit -m "원하는 메세지"
[main (root-commit) b315403] 원하는 메세지
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 first.txt
```

-m 옵션을 통해 메세지 내용을 등록할 수 있다. 메세지의 경우 작성 규칙은 없지만 대부분 메세지 앞에 `Add:`, `Update:`, `Modify:`, `Delete:` 와 같은 단어를 두고 변경 사항에 대해 설명하는 메세지를 적는다. 

```powershell
$ git log
commit b3154033ff0febde812dec56f6128042454da6db (HEAD -> main)
Author: Gaeun <mihara0309@gmail.com>
Date:   Fri Feb 11 22:45:49 2022 +0900

    Add: first text file
```

`$git log` 를 통해 커밋 메세지, 작성자, 변경 날자에 대한 정보가 출력된다.

### Github 가입하기

github는 온라인 git 저장소로 public과 private 저장소를 생성할 수 있다. organizetion이 지원되어 조직을 생성해 여러 사람들과 한 공간에서 다양한 프로젝트를 작업할 수 있도록 한다.

## 3. github과 함께

### 원격 저장소에 연결하기

```powershell
$ git remote add origin 복사한_자신의_git_url
```

github repogitory를 생성한 뒤 위와 같은 커맨드로 origin 이름으로 로컬 저장소를 github 저장소에 연결합니다. 이로써 push, pull 과 같은 명령어를 사용할 수 있게 되었습니다.

### github에 커밋 push하기

```powershell
$ git push origin main
```

git push 명령을 통해 origin(Github에 만든 저장소)의 main 브랜치에 커밋 내용을 반영

(원래는 Username과 Password를 입력해야 하지만 에러가 떠서 SSH-Key를 등록하고 반영했다.)

### 원격 저장소에서 새로운 내용 가져오기

```powershell
$ git pull
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
Unpacking objects: 100% (3/3), 691 bytes | 62.00 KiB/s, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
From github.com:KimGaeun309/github-practice
   b315403..093fc15  main       -> origin/main
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> main
$ git branch --set-upstream-to=origin/main main
branch 'main' set up to track 'origin/main'.
$ git pull
Updating b315403..093fc15
Fast-forward
 new_file.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 new_file.txt
$ git log
commit 093fc15c0e8dd477b006297ae52b1faa8a6acc44 (HEAD -> main, origin/main)
Author: KimGaeun309 <90085690+KimGaeun309@users.noreply.github.com>
Date:   Sat Feb 12 00:32:29 2022 +0900

    Add new_file

commit b3154033ff0febde812dec56f6128042454da6db
Author: Gaeun <mihara0309@gmail.com>
Date:   Fri Feb 11 22:45:49 2022 +0900

    Add: first text file
```

git pull 명령을 통해 remote 저장소 내용을 가져올 수 있다.

(명령이 안먹어서 `$ git branch --set-upstream-to=origin/main main` 을 통해 로컬 main이 origin/main을 추적하도록 만든 후 다시 `$ git pull` 을 실행시켰다.)

그리고 `$ git log` 통해 브랜치 커밋 내역을 확인하면 2개의 커밋을 확인할 수 있다.

### 다른 프로젝트 가져오기

```bash
$ git clone 가져오고_싶은_저장소_url
```

### git, 어려워서 못 쓰겠어요

Git Desktop을 통해 GUI로 쉽게 사용할 수 있다.

## 4. git 브랜치 사용

### 여러 명이서 작업한다면?

협업을 하면서 main 브랜치만 사용한다면 같은 이름의 파일에 대해 두 번 생성하는 등 충돌이 발생할 수 있다. 또 하나의 브랜치에서 기능을 여러 개 만들어 저장한다면 초기에 만든 기능에서 문제가 발생했을 경우 최근에 만든 문제가 없는 기능까지 되돌려야할 수 있다. 따라서 대다수의 프로젝트에서는 여러 개의 브랜치를 이용해 사람마다, 기능마다 나누어 작업하고 있다. 

### Branch와 checkout

```powershell
$ git branch develop
$ git checkout develop
Switched to branch 'develop'
$ git log
commit 093fc15c0e8dd477b006297ae52b1faa8a6acc44 (HEAD -> develop, origin/main, main)
```

`$ git branch develop` 으로 develop 이름의 새로운 브랜치 생성할 수 있다. branch는 git이 가리키는 위치(HEAD)에서 생성된다. `$ git checkout develop` 통해 브랜치를 전환할 수 있다. `$ git log` 로 HEAD(현재 git이 가리키는 위치)가 develop으로 바뀌어 있음을 확인할 수 있다.

### 다른 브랜치로 코드 합치기

작업 내용을 하나로 병합하는 merge

```powershell
$ git add file2.txt
$ git commit -m "Add: file2"
$ push origin develop
```

이전 내용까지 배운 명령을 이용해 Github의 develop 브랜치로 push한다. 현재 로컬 저장소가 develop인 경우 git push 명령을 하여도 origin의 develop으로 푸쉬된다. 

이를 병합하려면 github에서 `Compare&Pull Request` 를 누른다. base는 어느 브랜치에 합칠지, compare는 어느 브랜치를 합치는지. 이 두 가지를 설정한 다음 `Create pull request` 를 누른다. 다음 화면에서 협업을 하는 경우 병합 전에 코드 리뷰를 진행할 수 있다. `Merge pull request` 를 누르면 merge가 진행된다.

**추가 강의 자료**

[lesson.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/40c5335a-40d4-4532-9c64-b5419ed4451c/lesson.pdf)
