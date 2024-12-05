from nicegui import ui

ui.icon('thumb_up', color='primary').classes('text-5xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Carlos').style('color: #3BE0A8; font-family: Arial; font-size: 20px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()