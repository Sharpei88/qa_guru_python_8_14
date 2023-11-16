import os

from selene import browser, have, be


def test_fill_registration_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Vitalii')
    browser.element('#lastName').should(be.blank).type('Sharov')
    browser.element('#userEmail').should(be.blank).type('vitalii@example.com')

    browser.all('label[for^="gender-radio"]').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('.react-datepicker__month-select').should(be.visible).click().element(
                    'option[value="5"]').should(be.visible).click()
    browser.element('.react-datepicker__year-select').should(be.visible).click().element(
                    'option[value="1988"]').should(be.visible).click()
    browser.element('.react-datepicker__header :nth-child(1)').should(have.exact_text('June 1988'))
    browser.element('.react-datepicker__day--026').should(be.visible).click()
    browser.element('#dateOfBirthInput').should(have.value('26 Jun 1988'))

    browser.element('#subjectsInput').type('m')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Maths')).click()

    browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('Maths'))

    browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/23.jpg'))

    browser.element('#currentAddress').type('Long address for checking the address \n'
                                            ' entry form and entering it into the test \n'
                                            ' with line breaks')

    browser.element('#react-select-3-input').type('Har').press_enter()
    browser.element('#react-select-4-input').type('Ka').press_enter().press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('tbody').all('tr')[0].should(have.text('Vitalii Sharov'))
    browser.element('tbody').all('tr')[1].should(have.text('vitalii@example.com'))
    browser.element('tbody').all('tr')[2].should(have.text('Male'))
    browser.element('tbody').all('tr')[3].should(have.text('1234567890'))
    browser.element('tbody').all('tr')[4].should(have.text('26 June,1988'))
    browser.element('tbody').all('tr')[5].should(have.text('Maths'))
    browser.element('tbody').all('tr')[6].should(have.text('Sports'))
    browser.element('tbody').all('tr')[7].should(have.text('23.jpg'))
    browser.element('tbody').all('tr')[8].should(have.text('Long address for checking the address entry form and entering it into the test with line breaks'))
    browser.element('tbody').all('tr')[9].should(have.text('Haryana Karnal'))