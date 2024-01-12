import numpy as np
import statistics
import pandas as pd

#Replace the file path with the path the recorded movement dataset is stored
GAME = pd.read_excel('filepath', sheet_name = None)

#Use game_data as the input to all below functions
game_data = list(GAME.values())

#fix the missing data on the type column
def fill_type(data):
  Value = data[0]['Type'].unique()
  for df in data:
    df['Type'] = df['Type'].replace(Value[1], method = 'ffill')
    df['Type'] = df['Type'].replace(Value[4], Value[5])

#Extract the main phase of the data
def main_data(data):
  main = []
  Value = data[0]['Type'].unique()
  for df in data:
    main.append(df[df['Type'] == Value[-3]])
  return main

#Calculating IVA features.
def idx():
  trial = 'AVAAVVVVAAVAAVAVVAVAAAVAVAVVVAVAAAVVAAVVAVAAAVAVVV'*8
  auditory_idx = np.array([i.start() for i in re.finditer('A', trial)])
  visual_idx = np.array([i.start() for i in re.finditer('V', trial)])
  return [auditory_idx, visual_idx]

def Prudence(data):
  auditory_prudence = []
  visual_prudence = []
  error_idx = np.array([6, 12, 19, 26, 31, 38, 44, 49, 51, 106, 112, 119, 126, 131, 138, 144, 149, 151,
      206, 212, 219, 226, 231, 238, 244, 249, 251, 306, 312, 319, 326, 331, 338, 344, 349, 351,
      52, 53, 152, 153, 252, 253, 352, 353, 59, 61, 68, 73, 80, 85, 87, 91, 155, 159, 161,
      168, 173, 180, 185, 187, 191, 255, 259, 261, 268, 273, 280, 285, 287, 291,
      355, 359, 361, 368, 373, 380, 385, 387, 3])-1
  [auditory_idx, visual_idx] = idx()
  aud_error = np.intersect1d(auditory_idx, error_idx)
  vis_error = np.intersect1d(visual_idx, error_idx)
  Main = main_data(data)
  for df in Main:
    aud_data = df.iloc[list(aud_error)]
    aud = aud_data[aud_data['Response'] == '  comission error  '].shape[0]
    auditory_prudence.append(100-((aud/44)*100))

    vis_data = df.iloc[list(vis_error)]
    vis = vis_data[vis_data['Response'] == '  comission error  '].shape[0]
    visual_prudence.append(100-((vis/35)*100))
  return [auditory_prudence, visual_prudence]

def Vigilance(data):
  auditory_vigilance = []
  visual_vigilance = []
  error_idx = np.array([56, 62, 69, 76, 81, 88, 94, 99, 101, 102,
              156, 162, 169, 176, 181, 188, 194, 199, 201, 202,
              256, 262, 269, 276, 281, 288, 294, 299, 301, 302,
              356, 362, 369, 376, 381, 388, 394, 399, 13, 20, 27, 32, 39, 45, 50,
              107, 113, 120, 127, 132, 139, 145, 150,
              207, 213, 220, 227, 232, 239, 245, 250,
              307, 313, 320, 327, 332, 339, 345, 350])-1
  [auditory_idx, visual_idx] = idx()
  aud_error = np.intersect1d(auditory_idx, error_idx)
  vis_error = np.intersect1d(visual_idx, error_idx)
  Main = main_data(data)
  for df in Main:
    aud_data = df.iloc[list(aud_error)]
    aud = aud_data[aud_data['Response'] == '  omission error  '].shape[0]
    auditory_vigilance.append(100-((aud/35)*100))

    vis_data = df.iloc[list(vis_error)]
    vis = vis_data[vis_data['Response'] == '  omission error  '].shape[0]
    visual_vigilance.append(100-((vis/34)*100))




  return [auditory_vigilance, visual_vigilance]

def Comprehension(data):
  auditory_comp = []
  visual_comp = []
  error_idx = np.array([54, 55, 57, 58, 60, 63, 64, 65, 66, 67, 70, 71, 72, 74,
                        75, 77, 78, 79, 82, 83, 84, 86, 89, 90, 92, 93, 95, 96, 97, 98, 100,
                        154, 157, 158, 160, 163, 164, 165, 166, 167, 170, 171, 172, 174, 175,
                        177, 178, 179, 182, 183, 184, 186, 189, 190, 192, 193, 195, 196, 197, 198, 200,
                        254, 257, 258, 260, 263, 264, 265, 266, 267, 270, 271, 272, 274, 275, 277, 278, 279, 282,
                        283, 284, 286, 289, 290, 292, 293, 295, 296, 297, 298, 300, 354, 357, 358, 360, 363, 364,
                        365, 366, 367, 370, 371, 372, 374, 375, 377, 378, 379, 382, 383, 384, 386, 389, 390, 392, 393, 395,
                        396, 397, 398, 400, 1, 2, 3, 4, 5, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25,
                        28, 29, 30, 33, 34, 35, 36, 37, 40, 41, 42, 43, 46, 47, 48, 103, 104, 105, 108, 109, 110,
                        111, 114, 115, 116, 117, 118, 121, 122, 123, 124, 125, 128, 129, 130, 133, 134, 135, 136,
                        137, 140, 141, 142, 143, 146, 147, 148, 203, 204, 205, 208, 209, 210, 211, 214, 215, 216, 217,
                        218, 221, 222, 223, 224, 225, 228, 229, 230, 233, 234, 235, 236, 237, 240, 241, 242, 243, 246, 247, 248,
                        303, 304, 305, 308, 309, 310, 311, 314, 315, 316, 317, 318, 321, 322, 323, 324, 325, 328,
                        329, 330, 333, 334, 335, 336, 337, 340, 341, 342, 343, 346, 347, 348])-1
  [auditory_idx, visual_idx] = idx()
  aud_error = np.intersect1d(auditory_idx, error_idx)
  vis_error = np.intersect1d(visual_idx, error_idx)
  Main = main_data(data)
  for df in Main:
    aud_data = df.iloc[list(aud_error)]
    aud = aud_data[(aud_data['Response'] == '  omission error  ') | (aud_data['Response'] == '  comission error  ')].shape[0]
    auditory_comp.append(100-((aud/121)*100))

    vis_data = df.iloc[list(vis_error)]
    vis = vis_data[(vis_data['Response'] == '  omission error  ') | (vis_data['Response'] == '  comission error  ')].shape[0]
    visual_comp.append(100-((vis/130)*100))



  return [auditory_comp, visual_comp]

def Consistency(data):
  consistencyA = []
  consistencyV = []
  Main = main_data(data)
  for df in Main:

    reaction_timeA = list(df[((df['Response'] == '  Hit  ') | (df['Response'] == '  comission error  ')) &
                 ((df['Mode'] == '  Fish Auditory  ') | (df['Mode'] == '  Shark Auditory  '))]['ReactionTime'])
    q1_A = np.percentile(reaction_timeA, 25)
    q3_A = np.percentile(reaction_timeA, 75)
    consistencyA.append((q1_A/q3_A)*100)

    reaction_timeV = list(df[((df['Response'] == '  Hit  ') | (df['Response'] == '  comission error  ')) &
                 ((df['Mode'] == '  Fish Visual  ') | (df['Mode'] == '  Shark Visual  '))]['ReactionTime'])
    q1_V = np.percentile(reaction_timeV, 25)
    q3_V = np.percentile(reaction_timeV, 75)
    consistencyV.append((q1_V/q3_V)*100)

  return [consistencyA, consistencyV]

def Stamina(data):
  StaminaA = []
  StaminaV = []
  Main = main_data(data)
  for df in Main:
    df1 = df.head(n = 200)
    Auditory_mean1 = statistics.mean(list(df1[(df1['Response'] == '  Hit  ') &
             ((df1['Mode'] == '  Fish Auditory  ') | (df1['Mode'] == '  Shark Auditory  '))]['ReactionTime']))

    Visual_mean1 = statistics.mean(list(df1[(df1['Response'] == '  Hit  ') &
                 ((df1['Mode'] == '  Fish Visual  ') | (df1['Mode'] == '  Shark Visual  '))]['ReactionTime']))

    df2 = df.tail(n = 200)
    Auditory_mean2 = statistics.mean(list(df2[(df2['Response'] == '  Hit  ') &
                 ((df2['Mode'] == '  Fish Auditory  ') | (df2['Mode'] == '  Shark Auditory  '))]['ReactionTime']))


    Visual_mean2 = statistics.mean(list(df2[(df2['Response'] == '  Hit  ') &
                 ((df2['Mode'] == '  Fish Visual  ') | (df2['Mode'] == '  Shark Visual  '))]['ReactionTime']))

    StaminaA.append((Auditory_mean1/Auditory_mean2)*100)
    StaminaV.append((Visual_mean1/Visual_mean2)*100)

  return [StaminaA, StaminaV]

def Focus(data):

  FocusA = []
  FocusV = []
  Main = main_data(data)

  for df in Main:
    reaction_timeA = list(df[((df['Response'] == '  Hit  ') | (df['Response'] == '  comission error  ')) &
                 ((df['Mode'] == '  Fish Auditory  ') | (df['Mode'] == '  Shark Auditory  '))]['ReactionTime'])
    FocusA.append((1 - (statistics.pstdev(reaction_timeA)/statistics.mean(reaction_timeA)))*100)

    reaction_timeV = list(df[((df['Response'] == '  Hit  ') | (df['Response'] == '  comission error  ')) &
                 ((df['Mode'] == '  Fish Visual  ') | (df['Mode'] == '  Shark Visual  '))]['ReactionTime'])
    FocusV.append((1 - (statistics.pstdev(reaction_timeV)/statistics.mean(reaction_timeV)))*100)

  return [FocusA, FocusV]

def Speed(data):
  SpeedA = []
  SpeedV = []
  Main = main_data(data)
  for df in Main:
      reaction_timeA = list(df[((df['Response'] == '  Hit  ') &
                 ((df['Mode'] == '  Fish Auditory  ') | (df['Mode'] == '  Shark Auditory  ')) &
                  (df['middleMiddle'] == 1) & (df['ReactionTime'] > 0.125))]['ReactionTime'])
      SpeedA.append(statistics.mean(reaction_timeA))

      reaction_timeV = list(df[((df['Response'] == '  Hit  ') &
                 ((df['Mode'] == '  Fish Visual  ') | (df['Mode'] == '  Shark Visual  ')) &
                  (df['middleMiddle'] == 1) & (df['ReactionTime'] > 0.125))]['ReactionTime'])

      SpeedV.append(statistics.mean(reaction_timeV))

  return [SpeedA, SpeedV]

def Persistance(data):
  PersistanceA = []
  PersistanceV = []
  for df in data:
    reaction_time_warmA = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'WarmUp2  '))]['ReactionTime']))

    reaction_time_coolA = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'CoolDown2  '))]['ReactionTime']))

    PersistanceA.append(statistics.mean(reaction_time_warmA[0:3])/statistics.mean(reaction_time_coolA[0:3]))

    reaction_time_warmV = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'WarmUp1  '))]['ReactionTime']))

    reaction_time_coolV = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'CoolDown1  '))]['ReactionTime']))
    PersistanceV.append(statistics.mean(reaction_time_warmV[0:3])/statistics.mean(reaction_time_coolV[0:3]))

  return [PersistanceA, PersistanceV]


def Sensory(data):
  SensoryA = []
  SensoryV = []
  for df in data:
    reaction_timeA = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'WarmUp2  '))]['ReactionTime']))

    SensoryA.append(statistics.mean(reaction_timeA[0:3]))

    reaction_timeV = sorted(list(df[((df['Response'] == '  Hit  ') &
                              (df['Type'] == 'WarmUp1  '))]['ReactionTime']))

    SensoryV.append(statistics.mean(reaction_timeV[0:3]))
  return [SensoryA, SensoryV]

def Hyperactivity(data):
  OK = []
  LRT = []
  XCL = []
  Main = main_data(data)
  for df in Main:
    OK.append(df[(df['ReactionTime'] > 0.125) & (df['middleMiddle'] == 1)].shape[0])
    LRT.append(df[(df['ReactionTime'] <= 0.125) & (df['middleMiddle'] < 3)].shape[0])
    XCL.append(df[((df['ReactionTime'] > 0.125) & (df['middleMiddle'] == 2)) | (df['middleMiddle'] >= 3)].shape[0])
  return [OK, LRT, XCL]

