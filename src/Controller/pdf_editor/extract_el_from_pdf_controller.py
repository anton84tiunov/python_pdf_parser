import logging

import src.View.my_widgets.pdf_editor.interact.pdf_editor_interact as pdf_editor_interact
import src.Model.pdf_editor.extract_el_from_pdf_page as extract_el_from_pdf_page
import src.Model.pdf_editor.convert_pdf_el_to_model as convert_pdf_el_to_model
import src.Model.general.draw_model as drawModel
import src.Model.general.text_model as textModel
import src.Model.general.image_model as imageModel
class ExtractElFromPdfController():
    def __init__(self, root):
        self.root = root

        self.extr = extract_el_from_pdf_page.ExtractElFromPdf()
        self.conv = convert_pdf_el_to_model.ConvertPdfElToModel()

    def open_pdf(self, path, num_page) -> tuple[tuple, list[drawModel.DrawModel], list[textModel.TextModel], list[imageModel.ImageModel]]:
        logger = logging.getLogger('app.pdf_editor_controller')
        try:
            doc = self.extr.get_doc(path)
            page = self.extr.get_page(doc, num_page)
            el =  self.extr.get_el(doc, page)
            el_rect = el["rect"]
            el_draw = self.conv.conv_draws(el["draw"])
            el_text = self.conv.conv_texts(el["text"])
            el_img = self.conv.conv_images(el["image"])
            
            return el_rect, el_draw, el_text, el_img
        
        except Exception as e:
            logger.exception(e)
            # logging.basicConfig(filename='app_logs/pdf_editor.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # logging.warning(str(e))
            self.root.tab_pdf_editor.txt_brow_log.append(f'<span style=" font-family:"MS Shell Dlg 2"; font-size:5pt;color:#ff0000;"Error: </span><span style=" font-size:18pt; text-decoration: underline; color:#ffaa00;">{e}</span>')













