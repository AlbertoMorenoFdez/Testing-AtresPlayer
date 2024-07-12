from behave import *
from page_objects.common_steps_page import CommonStepsPage
from page_objects.play_content_page import PlayContentPage


@when(u'I access the feautured section of a channel and I click on a content')
def step_impl(context):
    context.alt_text = "La casa de empeños"
    play_content_page = PlayContentPage(context)

    try:
        play_content_page.acceder_a_la_casa_de_empenos()
        play_content_page.click_on_ver_ahora()
        play_content_page.click_on_ultima_temporada()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I should be able to play content from a channel from the featured section')
def step_impl(context):
    try:
        play_content_page = PlayContentPage(context)
        play_content_page.check_video_container()
    except Exception as e:
        print(f"Error: {e}")
