# -*- coding: utf-8 -*-
"""
Pocket Edition WebSocket API
"""
from typing import List, Iterable
from uuid import uuid1

# keys
key_head = 'header'
key_body = 'body'

head_or_body_ver = 'version'
head_or_prop_msg_type = 'MessageType'

ver = 1

# message types
msg_say = 'say'
msg_chat = 'chat'
msg_tell = 'tell'
msg_title = 'title'
msg_subtitle = 'subtitle'
msg_actionbar = 'actionbar'
msg_cmd_req = 'commandRequest'

head_msg_purpose = 'messagePurpose'
head_req_id = 'requestId'

# packet purposes
purpose_event = 'event'
purpose_error = 'error'
purpose_subscribe = 'subscribe'
purpose_unsubscribe = 'unsubscribe'
purpose_cmd_req = 'commandRequest'
purpose_cmd_resp = 'commandResponse'

body_props = 'properties'
body_status_code = 'statusCode'
body_status_msg = 'statusMessage'
body_event_name = 'eventName'
body_origin = 'origin'
body_input = 'input'
body_overload = 'overload'
body_cmdline = 'commandLine'
body_measurements = 'measurements'

# event names
event_app_paused = "AppPaused"
event_item_crafted = "ItemCrafted"
event_app_unpaused = "AppUnpaused"
event_store_promotion_note = "StorePromotionNotification"
event_world_imported = "WorldImported"
event_split_screen_updated = "SplitScreenUpdated"
event_edu_resources = "EduResources"
event_bell_block_used = "BellBlockUsed"
event_app_resumed = "AppResumed"
event_player_msg_say = "PlayerMessageSay"
event_player_bounced = "PlayerBounced"
event_purchase_game_attempt = "PurchaseGameAttempt"
event_trade_completed = "TradeCompleted"
event_treatments_set = "TreatmentsSet"
event_sign_in_to_xbox_live = "SignInToXboxLive"
event_world_unloaded = "WorldUnloaded"
event_lab_table_created = "LabTableCreated"
event_game_type_changed = "GameTypeChanged"
event_world_exported = "WorldExported"
event_responded_to_accept_content = "RespondedToAcceptContent"
event_ugc_down_started = "UgcDownloadStarted"
event_npc_props_updated = "NpcPropertiesUpdated"
event_start_client = "StartClient"
event_block_placed_by_cmd = "BlockPlacedByCommand"
event_script_ran = "ScriptRan"
event_storage = "Storage"
event_code_builder_down = "CodeBuilderDownload"
event_store_offer_purchase_failure = "StoreOfferPurchaseFailure"
event_behavior_failed = "BehaviorFailed"
event_signed_book_opened = "SignedBookOpened"
event_pack_imported_completed = "PackImportedCompleted"
event_multiplayer_session_update = "MultiplayerSessionUpdate"
event_world_history_pack_source_missing_during_upgrade = "WorldHistoryPackSourceMissingDuringUpgrade"
event_control_remapped_by_player = "ControlRemappedByPlayer"
event_dev_console_open = "DevConsoleOpen"
event_push_note_opened = "PushNotificationOpened"
event_pack_played = "PackPlayed"
event_pattern_added = "PatternAdded"
event_entitlement_list_info = "EntitlementListInfo"
event_structure_export = "StructureExport"
event_campfire_block_used = "CampfireBlockUsed"
event_cauldron_used = "CauldronUsed"
event_dweller_died = "DwellerDied"
event_game_rules_loaded = "GameRulesLoaded"
event_agent_cmd = "AgentCommand"
event_storage_report = "StorageReport"
event_content_shared = "ContentShared"
event_script_loaded = "ScriptLoaded"
event_multiplayer_connection_state_changed = "MultiplayerConnectionStateChanged"
event_multiplayer_round_start = "MultiplayerRoundStart"
event_first_time_client_open = "FirstTimeClientOpen"
event_respawn = "Respawn"
event_promotion_note_clicked = "PromotionNotificationClicked"
event_item_enchanted = "ItemEnchanted"
event_mob_born = "MobBorn"
event_ugc_down_completed = "UgcDownloadCompleted"
event_book_exported = "BookExported"
event_app_configuration_changed = "AppConfigurationChanged"
event_default_game_type_changed = "DefaultGameTypeChanged"
event_store_offer_purchase_attempt = "StoreOfferPurchaseAttempt"
event_player_transform = "PlayerTransform"
event_world_loaded = "WorldLoaded"
event_armor_stand_posed = "ArmorStandPosed"
event_popup_fired_edu = "PopupFiredEdu"
event_item_equipped = "ItemEquipped"
event_purchase_failure_details = "PurchaseFailureDetails"
event_menu_shown = "MenuShown"
event_player_teleported = "PlayerTeleported"
event_lectern_block_used = "LecternBlockUsed"
event_grindstone_block_used = "GrindstoneBlockUsed"
event_pack_upgrade_attempt = "PackUpgradeAttempt"
event_code_builder_closed = "CodeBuilderClosed"
event_performance_metrics = "PerformanceMetrics"
event_app_suspended = "AppSuspended"
event_player_msg_tell = "PlayerMessageTell"
event_level_dat_load_failed = "LevelDatLoadFailed"
event_player_msg_chat = "PlayerMessageChat"
event_book_image_imported = "BookImageImported"
event_cmd_block_edited = "CommandBlockEdited"
event_structure_generated = "StructureGenerated"
event_armor_stand_item_equipped = "ArmorStandItemEquipped"
event_level_destruct = "LevelDestruct"
event_chunk_changed = "ChunkChanged"
event_cartography_block_used = "CartographyBlockUsed"
event_experimental_gameplay = "ExperimentalGameplay"
event_pack_import_started = "PackImportStarted"
event_offer_rated = "OfferRated"
event_gameplay_tip_shown = "GameplayTipShown"
event_player_msg = "PlayerMessage"
event_trial_device_id_correlation = "TrialDeviceIdCorrelation"
event_compound_creator_created = "CompoundCreatorCreated"
event_copy_world_education_enabled = "CopyWorldEducationEnabled"
event_item_dropped = "ItemDropped"
event_jukebox_used = "JukeboxUsed"
event_popup_closed = "PopupClosed"
event_dweller_removed = "DwellerRemoved"
event_connection_failed = "ConnectionFailed"
event_item_destroyed = "ItemDestroyed"
event_player_join = "PlayerJoin"
event_boss_killed = "BossKilled"
event_unknown_block_received = "UnknownBlockReceived"
event_new_content_check_completed = "NewContentCheckCompleted"
event_fish_bucketed = "FishBucketed"
event_license_check = "LicenseCheck"
event_pet_died = "PetDied"
event_composter_block_used = "ComposterBlockUsed"
event_assert_failed = "AssertFailed"
event_set_multiplayer_correlation_id = "SetMultiplayerCorrelationId"
event_player_travelled = "PlayerTravelled"
event_purchase_resolved = "PurchaseResolved"
event_entity_interacted = "EntityInteracted"
event_behavior_errored = "BehaviorErrored"
event_dev_console_cmd = "DevConsoleCommand"
event_fixed_marketplace_world_using_v2_villagers_to_use_v1 = "FixedMarketplaceWorldUsingV2VillagersToUseV1"
event_portfolio_exported = "PortfolioExported"
event_item_named = "ItemNamed"
event_pack_hash_changed = "PackHashChanged"
event_incognito_failure = "IncognitoFailure"
event_element_constructor_used = "ElementConstructorUsed"
event_item_used = "ItemUsed"
event_realm_memberlist_cleared = "RealmMemberlistCleared"
event_player_msg_me = "PlayerMessageMe"
event_camera_used = "CameraUsed"
event_item_smelted = "ItemSmelted"
event_player_msg_title = "PlayerMessageTitle"
event_player_leave = "PlayerLeave"
event_search_catalog_req = "SearchCatalogRequest"
event_pattern_removed = "PatternRemoved"
event_float_prop_list = "FloatPropertyList"
event_set_valid_for_achievements = "SetValidForAchievements"
event_block_broken = "BlockBroken"
event_difficulty_set = "DifficultySet"
event_potion_brewed = "PotionBrewed"
event_join_canceled = "JoinCanceled"
event_world_generated = "WorldGenerated"
event_treatments_cleared = "TreatmentsCleared"
event_agent_created = "AgentCreated"
event_crafting_session_end = "CraftingSessionEnd"
event_client_id_created = "ClientIdCreated"
event_purchase_attempt = "PurchaseAttempt"
event_slash_cmd_executed = "SlashCommandExecuted"
event_crafting_session_start = "CraftingSessionStart"
event_entity_danced = "EntityDanced"
event_vehicle_exited = "VehicleExited"
event_item_acquired = "ItemAcquired"
event_start_world = "StartWorld"
event_chunk_loaded = "ChunkLoaded"
event_barrel_block_used = "BarrelBlockUsed"
event_treatment_pack_removed = "TreatmentPackRemoved"
event_book_copied = "BookCopied"
event_poi_block_usage_attempt = "POIBlockUsageAttempt"
event_cauldron_block_used = "CauldronBlockUsed"
event_content_logs_in_world_session = "ContentLogsInWorldSession"
event_end_of_day = "EndOfDay"
event_new_user_pack_detected = "NewUserPackDetected"
event_edui_o_s_purchase_transaction = "EduiOSPurchaseTransaction"
event_block_found = "BlockFound"
event_portal_used = "PortalUsed"
event_hw_info = "HardwareInfo"
event_reducer_block_entered = "ReducerBlockEntered"
event_sign_out_of_xbox_live = "SignOutOfXboxLive"
event_api_init = "ApiInit"
event_mob_killed = "MobKilled"
event_realm_url_generated = "RealmUrlGenerated"
event_portal_built = "PortalBuilt"
event_store_offer_clicked = "StoreOfferClicked"
event_entity_spawned = "EntitySpawned"
event_game_rules_updated = "GameRulesUpdated"
event_store_offer_purchase_resolved = "StoreOfferPurchaseResolved"
event_chunk_unloaded = "ChunkUnloaded"
event_caravan_changed = "CaravanChanged"
event_sign_in_edu = "SignInEdu"
event_treatment_pack_applied = "TreatmentPackApplied"
event_special_mob_built = "SpecialMobBuilt"
event_treatment_pack_downed = "TreatmentPackDownloaded"
event_upload_skin = "UploadSkin"
event_block_placed = "BlockPlaced"
event_book_edited = "BookEdited"
event_store_search = "StoreSearch"
event_board_text_updated = "BoardTextUpdated"
event_file_transmission_state = "FileTransmissionState"
event_player_saved = "PlayerSaved"
event_options_updated = "OptionsUpdated"
event_player_died = "PlayerDied"
event_push_note_received = "PushNotificationReceived"
event_push_note_permission = "PushNotificationPermission"
event_world_files_listed = "WorldFilesListed"
event_search_item_selected = "SearchItemSelected"
event_stack_loaded = "StackLoaded"
event_realm_shared = "RealmShared"
event_video_played = "VideoPlayed"
event_screen_changed = "ScreenChanged"
event_game_session_start = "GameSessionStart"
event_how_to_play_topic_changed = "HowToPlayTopicChanged"
event_edu_option_set = "EduOptionSet"
event_join_by_code = "JoinByCode"
event_mob_effect_changed = "MobEffectChanged"
event_award_achievement = "AwardAchievement"
event_skin_changed = "SkinChanged"
event_poi_block_used = "POIBlockUsed"
event_multiplayer_round_end = "MultiplayerRoundEnd"
event_heartbeat = "Heartbeat"
event_item_interacted = "ItemInteracted"
event_chat_sets_updated = "ChatSettingsUpdated"

all_events = [
    event_app_paused, event_item_crafted, event_app_unpaused, event_store_promotion_note, event_world_imported,
    event_split_screen_updated, event_edu_resources, event_bell_block_used, event_app_resumed, event_player_msg_say,
    event_player_bounced, event_purchase_game_attempt, event_trade_completed, event_treatments_set,
    event_sign_in_to_xbox_live, event_world_unloaded, event_lab_table_created, event_game_type_changed,
    event_world_exported, event_responded_to_accept_content, event_ugc_down_started, event_npc_props_updated,
    event_start_client, event_block_placed_by_cmd, event_script_ran, event_storage, event_code_builder_down,
    event_store_offer_purchase_failure, event_behavior_failed, event_signed_book_opened, event_pack_imported_completed,
    event_multiplayer_session_update, event_world_history_pack_source_missing_during_upgrade,
    event_control_remapped_by_player, event_dev_console_open, event_push_note_opened, event_pack_played,
    event_pattern_added, event_entitlement_list_info, event_structure_export, event_campfire_block_used,
    event_cauldron_used, event_dweller_died, event_game_rules_loaded, event_agent_cmd, event_storage_report,
    event_content_shared, event_script_loaded, event_multiplayer_connection_state_changed,
    event_multiplayer_round_start,
    event_first_time_client_open, event_respawn, event_promotion_note_clicked, event_item_enchanted, event_mob_born,
    event_ugc_down_completed, event_book_exported, event_app_configuration_changed, event_default_game_type_changed,
    event_store_offer_purchase_attempt, event_player_transform, event_world_loaded, event_armor_stand_posed,
    event_popup_fired_edu, event_item_equipped, event_purchase_failure_details, event_menu_shown,
    event_player_teleported,
    event_lectern_block_used, event_grindstone_block_used, event_pack_upgrade_attempt, event_code_builder_closed,
    event_performance_metrics, event_app_suspended, event_player_msg_tell, event_level_dat_load_failed,
    event_player_msg_chat, event_book_image_imported, event_cmd_block_edited, event_structure_generated,
    event_armor_stand_item_equipped, event_level_destruct, event_chunk_changed, event_cartography_block_used,
    event_experimental_gameplay, event_pack_import_started, event_offer_rated, event_gameplay_tip_shown,
    event_player_msg,
    event_trial_device_id_correlation, event_compound_creator_created, event_copy_world_education_enabled,
    event_item_dropped, event_jukebox_used, event_popup_closed, event_dweller_removed, event_connection_failed,
    event_item_destroyed, event_player_join, event_boss_killed, event_unknown_block_received,
    event_new_content_check_completed, event_fish_bucketed, event_license_check, event_pet_died,
    event_composter_block_used,
    event_assert_failed, event_set_multiplayer_correlation_id, event_player_travelled, event_purchase_resolved,
    event_entity_interacted, event_behavior_errored, event_dev_console_cmd, event_portfolio_exported, event_item_named,
    event_pack_hash_changed, event_incognito_failure, event_element_constructor_used, event_item_used,
    event_realm_memberlist_cleared, event_player_msg_me, event_camera_used, event_item_smelted, event_player_msg_title,
    event_player_leave, event_search_catalog_req, event_pattern_removed, event_float_prop_list,
    event_set_valid_for_achievements, event_block_broken, event_difficulty_set, event_potion_brewed,
    event_join_canceled,
    event_world_generated, event_treatments_cleared, event_agent_created, event_crafting_session_end,
    event_client_id_created, event_purchase_attempt, event_slash_cmd_executed, event_crafting_session_start,
    event_entity_danced, event_vehicle_exited, event_item_acquired, event_start_world, event_chunk_loaded,
    event_barrel_block_used, event_treatment_pack_removed, event_book_copied, event_poi_block_usage_attempt,
    event_cauldron_block_used, event_content_logs_in_world_session, event_end_of_day, event_new_user_pack_detected,
    event_edui_o_s_purchase_transaction, event_block_found, event_portal_used, event_hw_info,
    event_reducer_block_entered,
    event_sign_out_of_xbox_live, event_api_init, event_mob_killed, event_realm_url_generated, event_portal_built,
    event_store_offer_clicked, event_entity_spawned, event_game_rules_updated, event_store_offer_purchase_resolved,
    event_chunk_unloaded, event_caravan_changed, event_sign_in_edu, event_treatment_pack_applied,
    event_special_mob_built,
    event_treatment_pack_downed, event_upload_skin, event_block_placed, event_book_edited, event_store_search,
    event_board_text_updated, event_file_transmission_state, event_player_saved, event_options_updated,
    event_player_died,
    event_push_note_received, event_push_note_permission, event_world_files_listed, event_search_item_selected,
    event_stack_loaded, event_realm_shared, event_video_played, event_screen_changed, event_game_session_start,
    event_how_to_play_topic_changed, event_edu_option_set, event_join_by_code, event_mob_effect_changed,
    event_award_achievement, event_skin_changed, event_poi_block_used, event_multiplayer_round_end, event_heartbeat,
    event_item_interacted, event_chat_sets_updated
]

origin_type = 'type'

# origin types
origin_type_player = 'player'

# packet properties
prop_sender = 'Sender'
prop_receiver = 'Receiver'
prop_msg = 'Message'
prop_slot = 'Slot'
prop_type = 'Type'
prop_dna_ignore = 'DnaIgnore'
prop_player_game_mode = 'PlayerGameMode'
prop_block = 'Block'
prop_tool_item_type = 'ToolItemType'

# game modes
game_mode_survival = 0
game_mode_creative = 1
game_mode_adventure = 2

# slots
slot_armor_shield = 1
slot_armor_head = 2
slot_armor_chest = 3
slot_armor_legs = 4
slot_armor_feet = 5


def gen_pack(purpose: str) -> dict:
    """
    generate generic packet
    """
    return {
        key_head: {
            head_req_id: str(uuid1()),
            head_msg_purpose: purpose,
            head_or_body_ver: ver
        },
        key_body: {}
    }


def gen_sub(event_name: str, unsubscribe: bool = False) -> dict:
    """
    generate subscribe/unsubscribe event packet
    """
    new = {}
    if event_name:
        new = gen_pack(purpose_unsubscribe if unsubscribe else purpose_subscribe)
        head = get_head(new)
        head[head_or_prop_msg_type] = msg_cmd_req
        body = get_body(new)
        body[body_event_name] = event_name
    return new


def gen_all_subs(black_list: Iterable = None, unsubscribe: bool = False) -> List[dict]:
    """
    generate subscribe/unsubscribe all events packet
    """
    subs = []
    for event in all_events:
        if black_list:
            if event in black_list:
                continue
        subs.append(gen_sub(event, unsubscribe))
    return subs


def gen_cmd(cmdline: str) -> dict:
    """
    generate command packet
    """
    new = gen_pack(purpose_cmd_req)
    head = get_head(new)
    head[head_or_prop_msg_type] = msg_cmd_req
    body = get_body(new)
    body[head_or_body_ver] = ver
    body[body_origin] = {
        origin_type: origin_type_player
    }
    body[body_cmdline] = cmdline
    return new


def get_head(src: dict) -> dict:
    """
    get packet head
    """
    return src.get(key_head)


def get_body(src: dict) -> dict:
    """
    get packet body
    """
    return src.get(key_body)


def get_prop(body: dict) -> dict:
    """
    get packet body properties
    """
    return body.get(body_props)


def get_msg_purpose(head: dict) -> str:
    """
    get packet message purpose
    """
    return head.get(head_msg_purpose)


def get_head_ver(head: dict) -> str:
    """
    get packet version from header
    """
    return head.get(head_or_body_ver)


def get_body_ver(body: dict) -> str:
    """
    get packet version from body
    """
    return body.get(head_or_body_ver)


def get_event_name(body: dict) -> str:
    """
    get packet body event name
    """
    return body.get(body_event_name)


def get_msg_type(prop: dict) -> str:
    """
    get packet property message type
    """
    return prop.get(head_or_prop_msg_type)


def par_player_msg(prop: dict) -> (str, str):
    """
    parse player message packet properties
    """
    return (
        prop.get(prop_sender),
        prop.get(prop_receiver),
        prop.get(prop_msg)
    )


def par_cmd_resp_or_error(body: dict) -> (int, str):
    """
    parse command or error packet body
    """
    return (
        body.get(body_status_code),
        body.get(body_status_msg)
    )


def par_item_equipped(prop: dict) -> (int, str):
    """
    parse item equipped packet properties
    """
    return (
        prop.get(prop_slot),
        prop.get(prop_type)
    )


def par_item_used(prop: dict) -> str:
    """
    parse item used packet property
    """
    return prop.get(prop_type)


def par_block_destroyed(prop: dict) -> (str, str):
    """
    parse block destroyed packet properties
    """
    return (
        prop.get(prop_block),
        prop.get(prop_tool_item_type)
    )


def get_player_game_mode(prop: dict) -> int:
    """
    get player game mode from packet properties
    """
    return prop.get(prop_player_game_mode)


def is_new(prop: dict) -> bool:
    """
    detect backward compatible packet property
    """
    return prop.get(prop_dna_ignore, True)
