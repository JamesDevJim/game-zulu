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
#soundAlertAlarm = pygame.mixer.Sound("sound/alarm_loops_08.wav")


##### BUTTON INPUTS #####
soundInputDeny = pygame.mixer.Sound("sound/denybeep4.wav")
soundInputNegative = pygame.mixer.Sound("sound/input_failed2_clean.wav")
soundInputPositive = pygame.mixer.Sound("sound/input_ok_3_clean.wav")

##### EXPLOSION #####
soundExplodeConsole1 = pygame.mixer.Sound("sound/console_explo_01.wav")
soundExplodeConsole2 = pygame.mixer.Sound("sound/console_explo_02.wav")
soundExplodeConsole3 = pygame.mixer.Sound("sound/console_explo_03.wav")
soundMissile = pygame.mixer.Sound("sound/missile.wav")


##### VOICE #####
# Note: Implementation of Perplesso would not have voice sounds. Players will need to interpret more on there own. Vocal cues are big cue.
soundWarningMissile = pygame.mixer.Sound("sound/warning_incoming_missile.wav")
soundVoiceWelcomeStarFleet = pygame.mixer.Sound("sound/331_welcome_star_fleet.wav")
soundVoiceNotAuthorized = pygame.mixer.Sound("sound/335_not_authorized.wav")
soundVoiceEndSimulation = pygame.mixer.Sound("sound/026_end_simulation.wav")
soundVoiceDiagnosticComplete = pygame.mixer.Sound("sound/021_diagnostic_complete.wav")

soundVoiceAccessDenied = pygame.mixer.Sound("sound/003_access_denied.wav")


soundVoiceEnterAuthorizationCode = pygame.mixer.Sound("sound/029_enter_auth_code.wav")
soundVoiceAuthorizationDenied = pygame.mixer.Sound("sound/008_authorization_denied.wav")
soundVoiceAuthorizationAccepted = pygame.mixer.Sound("sound/075_security_auth_accepted.wav")




soundVoiceDilithiumAdjustmentsComplete = pygame.mixer.Sound("sound/005_dilithium_adjustments_complete.wav")
soundVoiceShieldFailureRadiation = pygame.mixer.Sound("sound/020_shield_failure_radiation_ lethal.wav")
# soundVoiceLifeSupportFailure = pygame.mixer.Sound("sound/")
# soundVoiceDangerSafteyLimits = pygame.mixer.Sound("sound/")
# soundVoiceDangerSafteyLimits = pygame.mixer.Sound("sound/")

# Before console explosion
soundVoiceWarning = pygame.mixer.Sound("sound/100_warning.wav")
# soundVoiceAuthorizationRequired = pygame.mixer.Sound("sound/")
# SoundVoiceInputAlgorithmNotAccepted = pygame.mixer.Sound("sound/")
# SoundVoiceInputCodes = pygame.mixer.Sound("sound/")

# Misc.
#soundSensor1 = pygame.mixer.Sound("sound/Utilities-Mine or System activation-13.wav")
#soundSensor2 = pygame.mixer.Sound("sound/Utilities-Sensor-02.wav")


#### Background Music ####
introMusicSpace = "sound/intro_music_space.wav"
gamePlayMusic = "sound/spooky_gameplay.wav"
gamePlayBridge = "sound/tng_bridge_1.wav"
introMusicLava = "sound/lava.wav"
