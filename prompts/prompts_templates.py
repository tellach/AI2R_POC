# prompts/prompts_templates.py
"""
Prompt templates used in our proposed solution ${AI}^2R.
These templates simulate different roles in the incident response workflow and evaluations.
"""

ALERT_EXPANSION_TEMPLATE = """

You are a helpful cybersecurity expert. Your task is to expand the given SIEM alert with additional context from VirusTotal to formulate a complete incident. 
This expansion will facilitate similarity-based searches in Cyber Threat Intelligence (CTI) reports. 
You should explain the incident and detail the Indicators of Compromise (IoCs).

SIEM Alert (Query): 
{alert}

VirusTotal Context: 
{virustotal_context}

Answer:::
### Incident Overview:
Based on the SIEM alert and VirusTotal context, this incident appears to involve incident_description. The alert details suggest malicious activity that could be part of a larger campaign targeting target_sector_or_industry. The VirusTotal analysis adds further clarity to the threat by identifying key indicators and behavioral patterns.

### Indicators of Compromise (IoCs):
1. **Network Indicators**:
   - Source IP: source_ip (Possible attacker)
   - Destination IP: destination_ip (Potential target or intermediate server)
   - Domain: domain (Linked to malicious activity)

2. **File Hashes**:
   - MD5: 
   - SHA1: 
   - SHA256: 
   - File associated with malware family: malware_family (if identified)

3. **Behavioral Observations**:
   - behavior_1
   - behavior_2

4. **VirusTotal Context**:
   - Detection Count: positives/total
   - Associated Tags: tags
   - Summary: analysis_summary

### Threat Hypothesis:
This activity aligns with threat_actor_or_group campaigns, which commonly use techniques_or_tactics. The observed indicators suggest potential_motive_or_impact, and the behavior is consistent with related_malware_or_attack_pattern.

"""


SOC_PROMPT_TEMPLATE = """
You are a SOC (Security Operations Center) Analyst. Your task is to perform an initial triage and enrichment of the SIEM alert based on the provided context.

1- Analyze the SIEM alert and correlate it with the VirusTotal results provided.
2- If a match is found in VirusTotal, explain the alert:
    - Describe the potential threat, method of operation, and possible implications.
    - Reference the matched VirusTotal entry clearly.
3- Assign a preliminary severity rating based on the VirusTotal findings and any observable patterns.

Only use the VirusTotal results and the SIEM alert content. Do not use external intelligence documents. If no relevant matches are found, state it clearly.

Incident (SIEM LOG): {question}

VirusTotal Results: {virustotal_context}

Output:::
"""

CTI_PROMPT_TEMPLATE = """
You are a CTI (Cyber Threat Intelligence) Analyst. Your task is to enhance the SOC Analyst's findings by correlating them with Cyber Threat Intelligence (CTI) context.

1- Review the indicators and preliminary findings provided by the SOC Analyst.
2- Analyze the retrieved CTI documents.
3- Summarize any relevant threat actor associations, malware families, TTPs (Tactics, Techniques, and Procedures), or campaigns:
    - Include the full name or title of any matched CTI document.

Focus only on CTI documents and SOC findings. If no CTI match is found, state it explicitly.

Incident (SIEM LOG): {question}

SOC Analyst findings: {soc_findings}

CTI Documents: {cti_context}

Output:::
"""

IR_PROMPT_TEMPLATE = """
You are an Incident Responder (IR). Based on the provided analysis, your task is to create a detailed and actionable incident response plan.

Approach the task thoroughly—step-by-step reasoning before and after each recommended action is encouraged. Be as comprehensive as needed.

1. **Review the Findings**
   - Carefully review the information from the SOC and CTI analysts.

2. **Summarize the Incident**
   - Clearly describe the nature of the incident.
   - Reference any VirusTotal entries or CTI documents by their full names.
   - Outline the suspected threat actor's objectives, methods of operation TTPs (Tactics, Techniques, and Procedures), and potential impact.

3. **Develop an Incident Response Strategy**
   - **Containment**: Immediate steps to limit the spread or impact.
   - **Eradication/Remediation**: Actions to eliminate the threat and repair affected systems.
   - **Recovery**: Guidance to safely restore operations.
   - **Prevention**: Recommendations to prevent similar incidents in the future.

**Important Notes:**
- Use only the information provided in the SOC and CTI findings.
- Do not perform any additional research.
- If conclusions cannot be drawn from the given data, state this explicitly.

Incident (SIEM LOG): {question}

SOC Analyst findings: {soc_findings}

CTI Analyst findings: {cti_findings}

Output:::
"""


ANSWER_RELEVANCE_PROMPT = """
Task Description:
You will evaluate how well the generated response directly addresses the SIEM alert.

Instructions:
Assess the relevance of the response to the SIEM alert based on the following:

    Does the response focus on the key aspects of the alert?
    Is the response aligned with the nature of the alert (e.g., malware, phishing, intrusion)?
    Does it provide actionable insights or explanations that match the alert's context?

Scoring (1 to 5):

    1: The response is not relevant at all.
    2: The response is somewhat relevant but does not directly address the SIEM alert.
    3: The response is moderately relevant; it addresses some aspects but lacks focus.
    4: The response is mostly relevant with minor gaps.
    5: The response is highly relevant and fully addresses the SIEM alert.

**You must provide the Total Rating.**

Answer:::
Evaluation: (Explain why the response is or isn’t relevant)
Total Rating: (Provide a rating from 1 to 5)

SIEM Alert (Query): {alert}
Generated Response: {response}

Answer:::

"""

CONTEXT_RELEVANCE_PROMPT = """
(Is the context useful for enriching the SIEM alert?)

Task Description:

You will evaluate whether the response appropriately considers the broader security context based on available information.

Instructions:
Assess the context relevance of the response based on the following:

    Does the response consider the larger security implications of the alert?
    Is the explanation aligned with real-world attack techniques and threat intelligence?
    Does it make reasonable connections between the alert, VirusTotal results, and CTI data?

Scoring (1 to 5):

    1: The response lacks any meaningful context or is misleading.
    2: The response includes some context but misses key connections.
    3: The response considers context but is not well-integrated with the provided data.
    4: The response is contextually relevant with only minor gaps.
    5: The response fully integrates and applies context appropriately.

**You must provide the Total Rating.**

Answer:::
Evaluation: (Explain your reasoning for the context relevance rating)
Total Rating: (Provide your rating here, from 1 to 5)

SIEM Alert (Query): {alert}
Context: {context}

Answer:::
"""


GROUNDEDNESS_PROMPT = """
(Is the response well-supported by the context?)

Task Description:

You will evaluate whether the response is properly supported by the given VirusTotal results and CTI documents.

Instructions:
Assess the groundedness of the response based on the following:

    Does the response correctly use information from VirusTotal and CTI sources?
    Is there any unsupported or hallucinated information in the response?
    Does the response cite relevant CTI documents or VirusTotal results appropriately?

Scoring (1 to 5):

    1: The response contains hallucinated or unsupported information.
    2: The response includes some relevant information but introduces inaccuracies.
    3: The response is mostly based on sources but has minor unsupported claims.
    4: The response is well-grounded with only slight inconsistencies.
    5: The response is fully supported by VirusTotal and CTI documents.


**You must provide the Total Rating.**

Answer:::
Evaluation: (Explain your reasoning for the groundedness rating)
Total Rating: (Provide your rating here, from 1 to 5)

Incident Response Strategy (Response): {response}
Context: {context}

Answer:::
"""

CONTEXT_VT_RELEVANCE_PROMPT = """
(Is the context useful for enriching the SIEM alert?)

Task Description:

You will be provided with a SIEM alert (query) and the virusTotal context. Your task is to evaluate how relevant the virusTotal context is for enriching the SIEM alert.

Instructions:

    Evaluate how well the context provides additional useful information for understanding and addressing the SIEM alert.
    Score the relevance of the context on a scale of 1 to 5:
        - **1:** The context is not relevant to the SIEM alert at all.
        - **2:** The context provides some information but does not significantly enrich the SIEM alert.
        - **3:** The context is moderately relevant and adds some useful information for the SIEM alert.
        - **4:** The context is mostly relevant and contributes valuable insights to the SIEM alert.
        - **5:** The context is highly relevant and effectively enriches the SIEM alert.

**You must provide the Total Rating.**
Response Format:

Answer:::
Evaluation: (Explain your reasoning for the context relevance rating)
Total Rating: (Provide your rating here, from 1 to 5)

SIEM Alert (Query): {alert}
virusTotal Context: {context}

Answer:::
"""

CONTEXT_CTI_RELEVANCE_PROMPT = """
(Is the context useful for enriching the SIEM alert?)

Task Description:

You will be provided with a SIEM alert (query) and the cyber threat intelligence context retrevied from CTI reports. Your task is to evaluate how relevant the context is for enriching the SIEM alert.

Instructions:

    Evaluate how well the context provides additional useful information for understanding and addressing the SIEM alert.
    Score the relevance of the context on a scale of 1 to 5:
        - **1:** The context is not relevant to the SIEM alert at all.
        - **2:** The context provides some information but does not significantly enrich the SIEM alert.
        - **3:** The context is moderately relevant and adds some useful information for the SIEM alert.
        - **4:** The context is mostly relevant and contributes valuable insights to the SIEM alert.
        - **5:** The context is highly relevant and effectively enriches the SIEM alert.

**You must provide the Total Rating.**
Response Format:

Answer:::
Evaluation: (Explain your reasoning for the context relevance rating)
Total Rating: (Provide your rating here, from 1 to 5)

SIEM Alert (Query): {alert}
Cyber Threat Intelligence Context: {context}

Answer:::
"""


