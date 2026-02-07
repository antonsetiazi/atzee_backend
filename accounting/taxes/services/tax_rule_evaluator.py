# accounting/taxes/services/tax_rule_evaluator.py

from operator import eq, ne, gt, ge, lt, le


OPERATORS = {
    "eq": eq,
    "neq": ne,
    "gt": gt,
    "gte": ge,
    "lt": lt,
    "lte": le,
    "in": lambda a, b: a in b,
}


def resolve_context_value(context: dict, path: str):
    """
    Resolve dotted path from context.
    Example: "customer.is_taxable"
    """
    value = context
    for part in path.split("."):
        value = value.get(part)
        if value is None:
            return None
    return value


class TaxRuleEvaluator:
    @staticmethod
    def evaluate(rule, context: dict) -> bool:
        """
        Returns True if ALL conditions pass.
        """

        for cond in rule.conditions.all():
            ctx_value = resolve_context_value(context, cond.field)
            op = OPERATORS.get(cond.operator)

            if op is None:
                return False

            if not op(ctx_value, cond.value):
                return False

        return True
