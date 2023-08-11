import streamlit as st
import pyshorteners
import clipboard
import webbrowser


class UrlShortenerApp:
    def __init__(self):
        self.s = pyshorteners.Shortener()

    def create(self, url):
        short_url = self.s.tinyurl.short(url)
        return short_url

    def copy_to_clipboard(self, short_url):
        clipboard.copy(short_url)

    def visit_short_url(self, short_url):
        webbrowser.open(short_url)


if __name__ == '__main__':
    st.title('URL Shortener')

    app = UrlShortenerApp()

    url = st.text_input('Paste Your URL Here:')
    if url:
        short_url = app.create(url)
        st.write('Shortened URL:', short_url)

        if st.button('Copy'):
            app.copy_to_clipboard(short_url)
            st.write('Copied to clipboard!')

        if st.button('Visit Short URL'):
            app.visit_short_url(short_url)

    st.write('---')
    st.write('Privacy and Security')
    st.write('We prioritize your privacy and data security. Your provided URLs are only used to generate short links and are not shared with third parties. Shortened URLs are not associated with any personal information. We use encryption to protect your data during transmission and storage. If you have any concerns, please feel free to contact us.')