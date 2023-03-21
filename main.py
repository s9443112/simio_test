import os
import sys

import clr  # @UnresolvedImport
# from clr import Convert

# TODO:: do some auto discovery here analogue to netlogo?
sys.path.append('C:/Program Files/Simio LLC/Simio')
clr.AddReference('SimioDLL')
clr.AddReference('SimioAPI')
import SimioAPI  # @UnresolvedImport
from System import DateTime
from datetime import datetime


project = SimioAPI.ISimioProject(SimioAPI.SimioProjectFactory.LoadProject("./file/simple_simio.spfx"))
models = SimioAPI.IModels(project.get_Models())
model = models.get_Item("簡易模型_資料串連CSV版")


# TODO:: 這個會無法觸發Data connection exporter 的事件
# experiment = SimioAPI.IExperiment(model.Experiments.Create('ema experiment'))'
# experiment.Run()

startTime = datetime.now()

# TODO:: 要使用DOTNET的DateTime
# model.RunSetup.StartingTime = DateTime(startTime.year, startTime.month, startTime.day, startTime.hour, startTime.minute, startTime.second)
model.RunSetup.StartingTime = DateTime(2023,9,1,0,0,0)

model.Plan.RunPlan()



