일정 관리 프로그램(Schedule Manager)
    <p>Docker와 Python(PyMySQL)을 사용하여 터미널 환경에서 일정을 관리(추가, 조회, 완료)할 수 있는 간단한 CLI 애플리케이션입니다.</p>
    
    <h2>✨ 주요 기능</h2>
    <ul>
        <li><strong>일정 추가:</strong> 제목, 설명, 시작/종료 시간을 입력하여 새로운 일정을 등록합니다.</li>
        <li><strong>일정 조회:</strong> 데이터베이스에 저장된 모든 일정을 목록 형태로 확인합니다.</li>
        <li><strong>일정 완료 처리:</strong> 특정 ID의 일정을 '완료' 상태로 변경합니다.</li>
    </ul>

    <h2>🛠️ 기술 스택</h2>
    <ul>
        <li><strong>언어:</strong> Python 3</li>
        <li><strong>데이터베이스:</strong> MySQL 8.0</li>
        [cite_start]<li><strong>라이브러리:</strong> PyMySQL [cite: 1][cite_start], Cryptography [cite: 1]</li>
        <li><strong>기타:</strong> Docker, Docker Compose, Makefile</li>
    </ul>
    
    <h2>🚀 시작하기</h2>
    <h3>사전 준비</h3>
    <p>이 프로젝트를 실행하기 위해서는 아래 프로그램들이 설치되어 있어야 합니다.</p>
    <ul>
        <li>Docker & Docker Compose</li>
        <li>Python 3.x</li>
    </ul>
    
    <h3>설치 및 실행 순서</h3>
    <ol>
        <li><strong>저장소 복제(Clone)</strong>
            <pre><code>git clone [저장소 URL]
CD [프로젝트 폴더]

Docker 컨테이너 실행
Makefile을 사용하여 MySQL 데이터베이스 서버를 시작합니다. init.sql파일에 정의된 대로 schedules테이블이 자동으로 생성됩니다.
make up
Python 클러스터 설치
setup.py 와 requirements.txt에베레스트를 설치합니다.
make install
프로그램 실행
[cite_start]일정 관리 프로그램을 시작합니다. [인용: 3]
make run
    <h2>⚠️ 중요: 코드 수정 안내</h2>
    <blockquote>
        <strong>참고:</strong> 제공된 `schedule_manager.py` 파일은 데이터베이스 스키마(`init.sql`)와 컬럼 이름이 일치하지 않아 오류가 발생합니다. (`completed` vs `is_completed`). 아래는 정상적으로 작동하도록 수정한 코드의 일부입니다.
    </blockquote>
    
    <p><b>schedule_manager.py</b> 파일의 <code>get_schedules</code>와 <code>complete_schedule</code> 함수를 아래와 같이 수정해야 합니다.</p>
    <pre><code># schedule_manager.py
def get_schedules(cursor: Cursor): """데이터베이스에서 모든 역할을 광대서 보기 출력합니다.""" # 'completed'를 'is_completed'로 수정 sql = "SELECT id, title, Description, start_datetime, end_datetime, is_completed FROM Schedules ORDER BY start_datetime" 커서.execute(sql) Schedules =cursor.fetchall()

if not schedules:
    print("\n-- 등록된 일정이 없습니다. --\n")
    return

print("\n--- 전체 일정 보기 ---")
for schedule in schedules:
    status = "✅ 완료" if schedule[5] else "□ 미완료"
    print(f"\n[ID: {schedule[0]}] {schedule[1]} ({status})")
    print(f"  - 설명: {schedule[2]}")
    print(f"  - 시간: {schedule[3]} ~ {schedule[4]}")
print("---------------------\n")
def Complete_schedule(cursor: Cursor): """특정 ID의 작업을 레버 처리합니다.""" # 'completed'를 'is_completed'로 수정 sql_select = "SELECT id, title FROM Schedules WHERE is_completed = FALSE ORDER BY id" 커서.execute(sql_select) Schedules =cursor.fetchall()

# ... (중략) ...

try:
    schedule_id = int(input("완료 처리할 일정의 ID를 입력하세요: "))
    # 'completed'를 'is_completed'로 수정
    sql_update = "UPDATE schedules SET is_completed = TRUE WHERE id = %s"
    updated_rows = cursor.execute(sql_update, (schedule_id,))
    
    # ... (이하 동일) ...
# ...
    <h2>📄 사용 가능한 명령어 (Makefile)</h2>
    [cite_start]<p>프로젝트 관리를 쉽게 하기 위해 `Makefile`에 여러 명령어들이 정의되어 있습니다. [cite: 2]</p>
    <ul>
        <li><code>make up</code>: Docker 컨테이너를 백그라운드에서 시작합니다.</li>
        <li><code>make down</code>: 실행 중인 Docker 컨테이너를 중지합니다.</li>
        <li><code>make logs</code>: MySQL 데이터베이스의 로그를 실시간으로 확인합니다.</li>
        <li><code>make status</code>: 컨테이너의 현재 상태를 확인합니다.</li>
        <li><code>make clean</code>: 컨테이너와 함께 데이터 볼륨까지 완전히 삭제합니다. (데이터베이스 초기화)</li>
        <li><code>make install</code>: 필요한 Python 패키지를 설치합니다.</li>
        [cite_start]<li><code>make run</code>: 파이썬 일정 관리 프로그램을 실행합니다. [cite: 4]</li>
    </ul>
</div>
