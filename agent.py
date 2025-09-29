from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from prompt import Refined_Prompt_1

from dotenv import load_dotenv
import os

load_dotenv()


s = """This my 68 sinals {"sender_known_malicios":1,
        "sender_domain_reputation_score":0.02,
        "sender_spoof_detected":1,
        "sender_temp_email_likelihood":0.95,
        "dmarc_enforced":0,
        "packer_detected":1,
        "any_file_hash_malicious":1,
        "max_metadata_suspicious_score":0.89,
        "malicious_attachment_Count":2,
        "has_executable_attachment":1,
        "unscannable_attachment_present":0,
        "total_yara_match_count":15,
        "total_ioc_count":23,
        "max_behavioral_sandbox_score":0.94,
        "max_amsi_suspicion_score":0.88,
        "any_macro_enabled_document":1,
        "any_vbscript_javascript_detected":1,
        "any_active_x_objects_detected":0,
        "any_network_call_on_open":1,
        "max_exfiltration_behavior_score":0.91,
        "any_exploit_pattern_detected":1,
        "total_embedded_file_count":3,
        "max_suspicious_string_entropy_score":0.92,
        "max_sandbox_execution_time":45.7,
        "unique_parent_process_names":"[\"cmd.exe\", \"powershell.exe\"]",
        "return_path_mismatch_with_from":1,
        "return_path_known_malicious":1,
        "return_path_reputation_score":0.03,
        "reply_path_known_malicious":1,
        "reply_path_diff_from_sender":1,
        "reply_path_reputation_Score":0.01,
        "smtp_ip_known_malicious":1,
        "smtp_ip_geo":0.98,
        "smtp_ip_asn":0.95,
        "smtp_ip_reputation_score":0.01,
        "domain_known_malicious":1,
        "url_Count":3,
        "dna_morphing_detected":1,
        "domain_tech_stack_match_score":0.95,
        "is_high_risk_role_targeted":1,
        "sender_name_similarity_to_vip":0.87,
        "urgency_keywords_present":1,
        "request_type":"wire_transfer",
        "content_spam_score":0.15,
        "user_marked_as_spam_before":0,
        "bulk_message_indicator":0,
        "unsubscribe_link_present":0,
        "marketing-keywords_detected":0.0,
        "html_text_ratio":0.1,
        "image_only_email":0,
        "spf_result":"fail",
        "dkim_result":"fail",
        "dmarc_result":"fail",
        "reverse_dns_valid":0,
        "tls_version":"TLS 1.0",
        "total_links_detected":3,
        "url_shortener_detected":1,
        "url_redirect_chain_length":4,
        "final_url_known_malicious":1,
        "url_decoded_spoof_detected":1,
        "url_reputation_score":0.02,
        "ssl_validity_status":"expired",
        "site_visual_similarity_to_known_brand":0.94,
        "url_rendering_behavior_score":0.89,
        "link_rewritten_through_redirector":0,
        "token_validation_success":0,
        "total_components_detected_malicious":5,
 } with classification labe is Mlicious"""


# Replace with your actual API key
API_KEY = os.getenv("API_KEY")

# Initialize LLM with API key
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0, api_key=API_KEY)

# System and user messages
system_message = SystemMessage(content=Refined_Prompt_1)
human_message = HumanMessage(content=s)

# Get response
response = llm([system_message, human_message])
print(response.content)
