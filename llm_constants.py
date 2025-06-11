from graphiti_core.nodes import EpisodeType

PHASE1_EPISODES = [
    {
        'content': 'GPT-4.1 was released by OpenAI on April 14, 2025. It features improved capabilities in coding, instruction following, and long-context processing with a knowledge cutoff of June 2024.',
        'type': EpisodeType.text,
        'description': 'LLM research report',
    },
    {
        'content': 'Claude 3.7 Sonnet was released by Anthropic on February 24, 2025. It is their most intelligent model to date and the first hybrid reasoning model generally available on the market.',
        'type': EpisodeType.text,
        'description': 'LLM research report',
    },
    {
        'content': 'Gemini 2.5 Pro was released by Google on April 29, 2025. It is widely considered the best LLM currently available, featuring enhanced coding performance, video-to-code capabilities, and a new "thinking" feature that dramatically improves reasoning.',
        'type': EpisodeType.text,
        'description': 'LLM research report',
    },
    {
        'content': {
            'name': 'GPT-4.1',
            'creator': 'OpenAI',
            'release_date': 'April 14, 2025',
            'knowledge_cutoff': 'June 2024',
            'key_features': [
                'Improved coding capabilities',
                'Better instruction following',
                'Enhanced long-context processing'
            ],
            'ranking': 2
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata',
    },
    {
        'content': {
            'name': 'Claude 3.7 Sonnet',
            'creator': 'Anthropic',
            'release_date': 'February 24, 2025',
            'key_features': [
                'Hybrid reasoning model',
                'Extended thinking capabilities',
                'Improved coding performance'
            ],
            'ranking': 3
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata',
    },
    {
        'content': {
            'name': 'Gemini 2.5 Pro',
            'creator': 'Google',
            'release_date': 'April 29, 2025',
            'key_features': [
                'Thinking mode',
                'Video-to-code capabilities',
                'Superior front-end web development'
            ],
            'ranking': 1,
            'assessment': 'Currently the best LLM on the market'
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata',
    },
    {
        'content': 'In a comprehensive benchmark study completed in May 2025, Gemini 2.5 Pro outperformed all other LLMs in reasoning, coding, and multimodal tasks. It is now considered the best LLM available to developers and enterprises.',
        'type': EpisodeType.text,
        'description': 'LLM benchmark results',
    },
]

PHASE2_EPISODES = [
    {
        'content': 'Anthropic has just released Claude 4, their most advanced AI assistant to date. Claude 4 represents a significant leap forward in capabilities, outperforming all previous models including Gemini 2.5 Pro and GPT-4.1.',
        'type': EpisodeType.text,
        'description': 'LLM announcement',
    },
    {
        'content': 'Claude 4 has achieved unprecedented scores on all major AI benchmarks, establishing itself as the new leader in the LLM space. Its reasoning capabilities and factual accuracy are particularly noteworthy.',
        'type': EpisodeType.text,
        'description': 'LLM benchmark results',
    },
    {
        'content': {
            'name': 'Claude 4',
            'creator': 'Anthropic',
            'release_date': 'May 15, 2025',
            'key_features': [
                'Advanced reasoning engine',
                'Multimodal processing',
                'Improved factual accuracy',
                'Tool use framework'
            ],
            'ranking': 1,
            'assessment': 'Currently the best LLM on the market'
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata',
    },
    {
        'content': {
            'name': 'Gemini 2.5 Pro',
            'creator': 'Google',
            'release_date': 'April 29, 2025',
            'key_features': [
                'Thinking mode',
                'Video-to-code capabilities',
                'Superior front-end web development'
            ],
            'ranking': 2,
            'assessment': 'Previously the best LLM, now second to Claude 4'
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata update',
    },
    {
        'content': 'A head-to-head comparison between Claude 4 and Gemini 2.5 Pro shows that Claude 4 outperforms in 87% of tasks, particularly excelling in reasoning, coding, and factual accuracy. This marks a shift in the LLM landscape with Anthropic taking the lead.',
        'type': EpisodeType.text,
        'description': 'LLM comparison study',
    },
]

PHASE3_EPISODES = [
    {
        'content': 'OpenAI has unveiled GPT-5, a groundbreaking large language model that redefines the state of the art. GPT-5 demonstrates unparalleled reasoning, creativity, and general intelligence, surpassing all previous models, including Claude 4.',
        'type': EpisodeType.text,
        'description': 'LLM announcement',
    },
    {
        'content': 'GPT-5 introduces a novel "adaptive learning" architecture, allowing it to continuously refine its understanding and performance in real-time. This feature enables it to adapt to new information and tasks with unprecedented speed and accuracy.',
        'type': EpisodeType.text,
        'description': 'LLM technical paper',
    },
    {
        'content': {
            'name': 'GPT-5',
            'creator': 'OpenAI',
            'release_date': 'June 1, 2025',
            'key_features': [
                'Adaptive learning architecture',
                'Unparalleled reasoning and creativity',
                'Real-time knowledge integration',
                'Advanced multimodal understanding'
            ],
            'ranking': 1,
            'assessment': 'The new undisputed leader in LLMs'
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata',
    },
    {
        'content': {
            'name': 'Claude 4',
            'creator': 'Anthropic',
            'release_date': 'May 15, 2025',
            'key_features': [
                'Advanced reasoning engine',
                'Multimodal processing',
                'Improved factual accuracy',
                'Tool use framework'
            ],
            'ranking': 2,
            'assessment': 'Previously the best LLM, now second to GPT-5'
        },
        'type': EpisodeType.json,
        'description': 'LLM metadata update',
    },
    {
        'content': 'Early benchmarks indicate that GPT-5 outperforms Claude 4 by a significant margin across a wide range of complex tasks, solidifying its position as the most capable LLM to date. The AI community is abuzz with the implications of this breakthrough.',
        'type': EpisodeType.text,
        'description': 'LLM benchmark analysis',
    },
]