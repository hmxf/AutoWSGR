# 任务调度功能，设置好后可以轮换练船，理论上可以无限轮换，直到手动停止

from autowsgr.fight.normal_fight import NormalFightPlan
from autowsgr.port.task_runner import FightTask, TaskRunner
from autowsgr.scripts.main import start_script


timer = start_script('./user_settings.yaml')
plan = NormalFightPlan(
    timer, 'C:/Users/Teruharu/Documents/GitHub/AutoWSGR/examples/plans/normal_fight/9-5BE.yaml'
)
runner = TaskRunner(timer)  # 注册 TaskRunner
runner.tasks.append(
    FightTask(
        timer,
        file_path='./fight_task.yaml',  # 任务配置文件路径，这个地方填写自己写好的配置文件
        plan=plan,
    ),
)  # 添加任务 (仅支持绝对路径)
runner.run()  # 启动调度器
