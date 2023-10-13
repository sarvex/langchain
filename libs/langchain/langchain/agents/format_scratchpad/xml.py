from typing import List, Tuple

from langchain.schema.agent import AgentAction


def format_xml(
    intermediate_steps: List[Tuple[AgentAction, str]],
) -> str:
    return "".join(
        f"<tool>{action.tool}</tool><tool_input>{action.tool_input}</tool_input><observation>{observation}</observation>"
        for action, observation in intermediate_steps
    )
