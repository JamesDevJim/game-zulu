import pygame

pygame.init()
pygame.mixer.init()

#### Sounds ####

# TODO: Get rid of these random sounds. This is space theme.
soundTrumpet = pygame.mixer.Sound("sound/trumpet.wav")
soundButtonPushDead = pygame.mixer.Sound("sound/button_push_dead.wav")
soundButtonDead = pygame.mixer.Sound("sound/button-10.wav")
soundButtonPush1 = pygame.mixer.Sound("sound/button_push_1.wav")
soundbuttonPush2 = pygame.mixer.Sound("sound/button_push_2.wav")

##### COMMON GAMEPLAY #####
#soundGameWelcome = 
soundGameDoors = pygame.mixer.Sound("sound/ds9_door.wav") # play when door opens and closes
soundGateSuccess = pygame.mixer.Sound("sound/sound_gate_success.wav") 
#soundGameFail = pygame.mixer.Sound("sound/")
#soundGameIntro = pygame.mixer.Sound("sound/")
#soundGameExit = pygame.mixer.Sound("sound/Shut_Off_Engine_SI_03.wav")

##### ALERTS #####
soundAlertCritical = pygame.mixer.Sound("sound/critical.wav")
soundAlertDamage = pygame.mixer.Sound("sound/damagealarm.wav")
soundAlertAlarm = pygame.mixer.Sound("sound/alarm_loops_08.wav")


##### BUTTON INPUTS #####
soundInputDeny = pygame.mixer.Sound("sound/denybeep4.wav")
soundInputNegative = pygame.mixer.Sound("sound/input_failed_clean.wav") # maybe pick one.
soundInputNegative = pygame.mixer.Sound("sound/input_failed2_clean.wav")
soundInputPositve = pygame.mixer.Sound("sound/input_ok_3_clean.wav")

##### EXPLOSION #####
soundExplodeConsole1 = pygame.mixer.Sound("sound/console_explo_01.wav")
soundExplodeConsole2 = pygame.mixer.Sound("sound/console_explo_02.wav")
soundExplodeConsole3 = pygame.mixer.Sound("sound/console_explo_03.wav")
soundMissile = pygame.mixer.Sound("sound/missile.wav")


##### Voice #####
# Note: Implementation of Perplesso would not have voice sounds. Players will need to interpret more on there own. Vocal cues are big cue.
soundWarningMissile = pygame.mixer.Sound("sound/warning_incoming_missile.wav")
# soundVoiceWelcome = pygame.mixer.Sound("sound/")
# soundVoiceAuthorizationRequired = pygame.mixer.Sound("sound/")
# soundVoiceAuthorizationAccepted = pygame.mixer.Sound("sound/")
# SoundVoiceInputAlgorithmNotAccepted = pygame.mixer.Sound("sound/")
# SoundVoiceInputCodes = pygame.mixer.Sound("sound/")

# Misc.
soundSensor1 = pygame.mixer.Sound("sound/Utilities-Mine or System activation-13.wav")
soundSensor2 = pygame.mixer.Sound("sound/Utilities-Sensor-02.wav")


#### Background Music ####
introMusicSpace = "sound/intro_music_space.wav"
gamePlayMusic = "sound/spooky_gameplay.wav"
gamePlayBridge = "sound/tng_bridge_1.wav"
introMusicLava = "sound/lava.wav"
