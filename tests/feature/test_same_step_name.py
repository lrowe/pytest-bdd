"""Different step types with the same name."""

from pytest_bdd import (
    scenario,
    then,
    when,
)


@scenario('same_step_name.feature', 'When and Then with same step name')
def test_when_and_then_with_same_step_name():
    pass


@then('I do something')
@when('I do something')
def i_do_something():
    pass
