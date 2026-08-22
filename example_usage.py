from client import EnterpriseAiDlpGovernanceGatewayClient

def main():
    client = EnterpriseAiDlpGovernanceGatewayClient()
    prompt = 'Analyze billing pattern for patient john.doe@hospital.org with card 4111-2222-3333-4444'
    res = client.inspect_and_mask_prompt(prompt, ['HIPAA', 'PCI_DSS'])
    print('DLP Verdict: ' + res['dlp_verdict'] + ' | Entities Masked: ' + str(res['pii_entities_redacted_count']))
    print('Sanitized Prompt: ' + res['sanitized_prompt'])
    print('Redactions:')
    for e in res['entities_redacted']:
        print('  [' + e['type'] + '] ' + e['original'] + ' -> ' + e['masked'])

if __name__ == '__main__':
    main()
