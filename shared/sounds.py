import pygame

pygame.init()
pygame.mixer.init()

#### Sounds ####

##### COMMON GAMEPLAY #####
soundGameDoors = pygame.mixer.Sound("sound/ds9_door.wav") # play when door opens and closes
#soundGameExit = pygame.mixer.Sound("sound/Shut_Off_Engine_SI_03.wav")

##### ALERTS #####
soundAlertCritical = pygame.mixer.Sound("sound/critical.wav")
soundAlertDamage = pygame.mixer.Sound("sound/damagealarm.wav")
soundAlertRedAlarm = pygame.mixer.Sound("sound/voy_redalert.wav")
#soundAlertAlarm = pygame.mixer.Sound("sound/alarm_loops_08.wav")

##### BUTTON INPUTS #####
soundInputDeny = pygame.mixer.Sound("sound/denybeep4.wav")
soundInputNegative = pygame.mixer.Sound("sound/input_failed2_clean.wav")
soundInputPositive = pygame.mixer.Sound("sound/input_ok_3_clean.wav")

##### EXPLOSION #####
soundExplodeConsole1 = pygame.mixer.Sound("sound/console_explo_01.wav")
soundExplodeConsole2 = pygame.mixer.Sound("sound/console_explo_02.wav")
soundExplodeConsole3 = pygame.mixer.Sound("sound/console_explo_03.wav")
soundExplodeSmall = pygame.mixer.Sound("sound/smallexplosion1.wav")
soundExplodeLarge = pygame.mixer.Sound("sound/largeexplosion2.wav")
soundMissile = pygame.mixer.Sound("sound/missile.wav")

##### VOICE #####
# General
soundVoiceWelcomeStarFleet = pygame.mixer.Sound("sound/331_welcome_star_fleet.wav")
soundVoiceDiagnosticComplete = pygame.mixer.Sound("sound/021_diagnostic_complete.wav")
soundVoiceWarning = pygame.mixer.Sound("sound/100_warning.wav")
soundVoiceUnableToComply = pygame.mixer.Sound("sound/unable_to_comply.wav")

# Authorization and Access
soundVoiceNotAuthorized = pygame.mixer.Sound("sound/335_not_authorized.wav")
soundVoiceEndSimulation = pygame.mixer.Sound("sound/026_end_simulation.wav")
soundVoiceAccessDenied = pygame.mixer.Sound("sound/003_access_denied.wav")
soundVoiceEnterAuthorizationCode = pygame.mixer.Sound("sound/029_enter_auth_code.wav")
soundVoiceAuthorizationDenied = pygame.mixer.Sound("sound/008_authorization_denied.wav")
soundVoiceAuthorizationAccepted = pygame.mixer.Sound("sound/075_security_auth_accepted.wav")

# Ship Functions
soundVoiceDilithiumAdjustmentsComplete = pygame.mixer.Sound("sound/005_dilithium_adjustments_complete.wav")
soundVoiceShieldFailureRadiation = pygame.mixer.Sound("sound/020_shield_failure_radiation_ lethal.wav")
soundVoiceAutoDefenseInitiated = pygame.mixer.Sound("sound/009_auto_defense_initiated.wav")
soundVoiceReloadCircuitsInitializing = pygame.mixer.Sound("sound/072_reload_circuits_initializing.wav")
soundVoiceWarpEnergyIncrease = pygame.mixer.Sound("sound/101_warp_energy_increase.wav")
soundVoiceInitiatingUpdate = pygame.mixer.Sound("sound/035_initiating_update.wav")
soundVoiceLifeSupportTerminated = pygame.mixer.Sound("sound/017_deck_lifesupport_terminated.wav")
# soundVoiceLifeSupportFailure = pygame.mixer.Sound("sound/")
# soundVoiceDangerSafteyLimits = pygame.mixer.Sound("sound/")
# soundVoiceAuthorizationRequired = pygame.mixer.Sound("sound/")
# SoundVoiceInputAlgorithmNotAccepted = pygame.mixer.Sound("sound/")
# SoundVoiceInputCodes = pygame.mixer.Sound("sound/")

# Misc.
soundTorpedoLoad = pygame.mixer.Sound("sound/loading_torpedo.wav")
soundTordedoFire = pygame.mixer.Sound("sound/torpedo_fire_clean.wav")
soundShipFlyBy = pygame.mixer.Sound("sound/borg_flyby.wav")

#### Background Music ####
introMusicSpace = "sound/intro_music_space.wav"
gamePlayMusic = "sound/spooky_gameplay.wav"
gamePlayBridge = "sound/tng_bridge_1.wav"
gamePlayShip = "sound/tng_lab.wav"
gamePlayShip2 = "sound/ship_noise.wav"

