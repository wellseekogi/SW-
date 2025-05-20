import zipfile
import string
import multiprocessing
import time
import itertools

# 설정
zip_file_path = '2-1-emergency_storage_key.zip'
first_chars = 'nopqrs'
other_chars = string.ascii_lowercase + string.digits
password_length = 6

# ZIP 파일 추출 시도 함수
def extract_zip(password):
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            zf.extractall(pwd=password.encode('utf-8'))
            return True
    except:
        return False

# 각 프로세스 작업
def worker(first_char, progress, total, found_flag, result_dict):
    for combo in itertools.product(other_chars, repeat=5):  # 나머지 5자리
        if found_flag.value:
            return
        candidate = first_char + ''.join(combo)
        if extract_zip(candidate):
            found_flag.value = True
            result_dict['password'] = candidate
            return
        with progress.get_lock():
            progress.value += 1

# 실시간 진행률 표시
def progress_monitor(progress, total, found_flag):
    start_time = time.time()
    while not found_flag.value:
        time.sleep(1)
        percent = (progress.value / total) * 100
        elapsed = time.time() - start_time
        print(f"\r⏳ 시도: {progress.value:,} / {total:,} ({percent:.2f}%) | 경과 시간: {elapsed:.1f}초", end='')

# 메인 실행
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    result_dict = manager.dict()
    progress = multiprocessing.Value('L', 0)
    found_flag = multiprocessing.Value('b', False)

    total_per_first = len(other_chars) ** 5
    total_combinations = len(first_chars) * total_per_first

    print(f"💻 사용 가능한 CPU 코어 수: {multiprocessing.cpu_count()}")
    print(f"🔡 첫 글자 후보: {first_chars}")
    print(f"🔢 나머지 조합 수 (한 글자당): {total_per_first:,}")
    print(f"📦 전체 비밀번호 조합 수: {total_combinations:,}\n")

    monitor = multiprocessing.Process(target=progress_monitor, args=(progress, total_combinations, found_flag))
    monitor.start()

    processes = []
    for fc in first_chars:
        p = multiprocessing.Process(target=worker, args=(fc, progress, total_combinations, found_flag, result_dict))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    monitor.terminate()

    if 'password' in result_dict:
        print(f"\n\n✅ 비밀번호를 찾았습니다: {result_dict['password']}")
    else:
        print("\n❌ 비밀번호를 찾지 못했습니다.")
