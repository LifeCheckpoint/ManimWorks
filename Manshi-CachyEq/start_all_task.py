import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def run_manimgl_command(script_name, scene_name):
    """
    执行单个 manimgl 命令的函数。
    """
    command = [
        "uv", "run", "manimgl",
        script_name,
        scene_name,
        "-w", "--uhd", "--fps", "120"
    ]
    command_str = " ".join(command)
    print(f"Executing: {command_str}")
    try:
        # 使用 subprocess.run 来执行命令，capture_output=True 可以捕获输出
        # check=True 会在命令返回非零退出码时抛出 CalledProcessError
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully executed: {command_str}")
        print(f"Stdout:\n{result.stdout}")
        if result.stderr:
            print(f"Stderr:\n{result.stderr}")
        return True, command_str, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command_str}")
        print(f"Return Code: {e.returncode}")
        print(f"Stdout:\n{e.stdout}")
        print(f"Stderr:\n{e.stderr}")
        return False, command_str, e.stdout, e.stderr
    except FileNotFoundError:
        print(f"Error: 'uv' command not found. Please ensure 'uv' is installed and in your PATH.")
        return False, command_str, "", "uv command not found"
    except Exception as e:
        print(f"An unexpected error occurred for command: {command_str}")
        print(f"Error details: {e}")
        return False, command_str, "", str(e)

def main():
    # 定义所有需要执行的任务
    # 每个元组包含 (script_name, scene_name)
    tasks = [
        ("CAPart2.py", "CAPart2_1"),
        ("CAPart2.py", "CAPart2_2"),
        ("CAPart2.py", "CAPart2_3"),
        # ("CAPart2.py", "CAPart2_4_3"),
        ("CAPart2.py", "CAPart2_5"),
        # ("CAPart2.py", "CAPart2_6"),
        ("CAPart3.py", "CAPart3_1"),
        ("CAPart3.py", "CAPart3_2_1"),
        ("CAPart3.py", "CAPart3_2_2"),
        ("CAPart4.py", "CAPart4_1"),
        ("CAPart4.py", "CAPart4_2"),
        ("CAPart4.py", "CAPart4_3"),
    ]

    # 设置最大并行进程数
    max_parallel_processes = 2

    # 使用 ThreadPoolExecutor 来管理并发执行
    # 注意：ThreadPoolExecutor 实际上是使用线程，但对于I/O密集型任务（如执行外部命令），
    # 线程通常是合适的。如果需要真正的进程并行（例如CPU密集型任务），应该使用 ProcessPoolExecutor。
    # 对于外部命令执行，线程池通常足够，因为Python GIL不影响外部进程的执行。
    with ThreadPoolExecutor(max_workers=max_parallel_processes) as executor:
        # 提交所有任务到执行器
        future_to_task = {executor.submit(run_manimgl_command, script, scene): (script, scene) for script, scene in tasks}

        # 迭代已完成的任务
        for future in as_completed(future_to_task):
            script, scene = future_to_task[future]
            try:
                success, command_str, stdout, stderr = future.result()
                if success:
                    print(f"Task '{script} {scene}' completed successfully.")
                else:
                    print(f"Task '{script} {scene}' failed.")
            except Exception as exc:
                print(f"Task '{script} {scene}' generated an exception: {exc}")

    print("\nAll tasks have been submitted and processed.")

if __name__ == "__main__":
    main()
