import logging
from functools import partial
from typing import Callable, List, Optional, Type

from declarai.operators.base.types import Message
from .base_task_operator import BaseOpenAITaskOperator
from .openai_llm import OpenAILLM

logger = logging.getLogger("OpenAITaskOperator")


class OpenAITaskOperator(BaseOpenAITaskOperator):
    llm: OpenAILLM
    compiled_template: List[Message]
    set_llm: Callable

    @classmethod
    def new_operator(
        cls,
        openai_token: Optional[str] = None,
        model: Optional[str] = None,
    ) -> Type["OpenAITaskOperator"]:
        openai_llm = OpenAILLM(openai_token, model)
        partial_class = partial(cls, openai_llm)
        return partial_class
