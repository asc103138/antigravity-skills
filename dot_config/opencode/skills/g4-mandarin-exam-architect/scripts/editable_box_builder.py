"""
Word 原生可編輯國字注音雙格方塊生成器 (editable_box_builder.py)
用途：
將國語考卷第一大題（寫出國字和注音）中的 28 個作答格建構為 Word 原生可編輯群組文字方塊 (wpg:wgp)，
取代傳統不可編輯的 .png 圖片方格。教師在 Word 中直接點擊左格即可修改國字、點擊右格即可修改注音。
"""

import os
import re
import zipfile


def make_box_xml(box_id, char_str, zhuyin_lines, test_type, is_answer_sheet=False):
    """
    產生單一 Word 原生可編輯「左國字、右注音」群組文字方塊 (<w:drawing> XML)。

    參數：
    - box_id (int): 唯一物件編號 (例如 101 ~ 128)
    - char_str (str): 國字正字，例如 '鷹'
    - zhuyin_lines (list[str]): 注音分行列表，聲母/介音單獨一行，韻母與聲調同行，例如 ['ㄈ', 'ㄤˇ'] 或 ['ㄔ', 'ㄨ', 'ㄥ']
    - test_type (str): 'char' (考國字，學生版左格留空) 或 'zhuyin' (考注音，學生版右格留空)
    - is_answer_sheet (bool): False 為學生版試卷，True 為參考答案卷（同時顯示國字與注音，考點標紅字 FF0000）
    """
    if not is_answer_sheet:
        disp_char = '' if test_type == 'char' else char_str
        disp_zy = zhuyin_lines if test_type == 'char' else ['']
        char_color = '000000'
        zy_color = '000000'
    else:
        disp_char = char_str
        disp_zy = zhuyin_lines
        char_color = 'FF0000' if test_type == 'char' else '000000'
        zy_color = 'FF0000' if test_type == 'zhuyin' else '000000'

    char_rpr = f'''<w:rPr>
      <w:rFonts w:ascii="標楷體" w:hAnsi="標楷體" w:eastAsia="標楷體"/>
      <w:color w:val="{char_color}"/>
      <w:sz w:val="46"/>
      <w:szCs w:val="46"/>
    </w:rPr>'''
    char_run = f'<w:r>{char_rpr}<w:t>{disp_char}</w:t></w:r>'

    n_lines = len(disp_zy) if disp_zy != [''] else 2
    if n_lines <= 2:
        line_twips = 210
        font_sz = 20  # 10pt
        spacing_val = -85
        ind_left = 18
    else:
        line_twips = 160
        font_sz = 17  # 8.5pt
        spacing_val = -75
        ind_left = 22

    zy_paras = []
    for line in disp_zy:
        zy_rpr = f'''<w:rPr>
          <w:rFonts w:ascii="標楷體" w:hAnsi="標楷體" w:eastAsia="標楷體"/>
          <w:color w:val="{zy_color}"/>
          <w:spacing w:val="{spacing_val}"/>
          <w:sz w:val="{font_sz}"/>
          <w:szCs w:val="{font_sz}"/>
        </w:rPr>'''
        zy_paras.append(f'''<w:p>
          <w:pPr>
            <w:snapToGrid w:val="0"/>
            <w:spacing w:before="0" w:after="0" w:line="{line_twips}" w:lineRule="exact"/>
            <w:ind w:left="{ind_left}" w:right="-150"/>
            <w:jc w:val="left"/>
            {zy_rpr}
          </w:pPr>
          <w:r>
            {zy_rpr}
            <w:t>{line}</w:t>
          </w:r>
        </w:p>''')

    zy_content = '\n'.join(zy_paras)

    return f'''<w:drawing>
  <wp:inline distT="0" distB="0" distL="0" distR="0">
    <wp:extent cx="584200" cy="406400"/>
    <wp:effectExtent l="0" t="0" r="0" b="0"/>
    <wp:docPr id="{box_id}" name="EditableBox_{box_id}"/>
    <wp:cNvGraphicFramePr/>
    <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
      <a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup">
        <wpg:wgp>
          <wpg:cNvGrpSpPr/>
          <wpg:grpSpPr>
            <a:xfrm>
              <a:off x="0" y="0"/>
              <a:ext cx="584200" cy="406400"/>
              <a:chOff x="0" y="0"/>
              <a:chExt cx="584200" cy="406400"/>
            </a:xfrm>
          </wpg:grpSpPr>
          <wps:wsp>
            <wps:cNvSpPr txBox="1"/>
            <wps:spPr>
              <a:xfrm>
                <a:off x="0" y="0"/>
                <a:ext cx="406400" cy="406400"/>
              </a:xfrm>
              <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
              <a:ln w="12700"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln>
            </wps:spPr>
            <wps:txbx>
              <w:txbxContent>
                <w:p>
                  <w:pPr>
                    <w:snapToGrid w:val="0"/>
                    <w:spacing w:before="0" w:after="0" w:line="440" w:lineRule="atLeast"/>
                    <w:jc w:val="center"/>
                    {char_rpr}
                  </w:pPr>
                  {char_run}
                </w:p>
              </w:txbxContent>
            </wps:txbx>
            <wps:bodyPr rot="0" vert="horz" wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="ctr" anchorCtr="0">
              <a:noAutofit/>
            </wps:bodyPr>
          </wps:wsp>
          <wps:wsp>
            <wps:cNvSpPr txBox="1"/>
            <wps:spPr>
              <a:xfrm>
                <a:off x="406400" y="0"/>
                <a:ext cx="177800" cy="406400"/>
              </a:xfrm>
              <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
              <a:ln w="12700"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln>
            </wps:spPr>
            <wps:txbx>
              <w:txbxContent>
                {zy_content}
              </w:txbxContent>
            </wps:txbx>
            <wps:bodyPr rot="0" vert="horz" wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="ctr" anchorCtr="0">
              <a:noAutofit/>
            </wps:bodyPr>
          </wps:wsp>
        </wpg:wgp>
      </a:graphicData>
    </a:graphic>
  </wp:inline>
</w:drawing>'''


def convert_docx_boxes(docx_path, items, is_answer_sheet=False):
    """
    將目標 .docx 中的 <w:drawing> 依序替換為可編輯方格，並清除舊的靜態圖片檔。
    items 格式: [(1, '彷', ['ㄈ', 'ㄤˇ'], 'char'), ...]
    """
    with zipfile.ZipFile(docx_path, 'r') as zin:
        doc_xml = zin.read('word/document.xml').decode('utf-8')
        parts = re.split(r'(<w:drawing>.*?</w:drawing>)', doc_xml, flags=re.DOTALL)
        drawing_indices = [i for i, p in enumerate(parts) if p.startswith('<w:drawing>')]
        assert len(drawing_indices) == len(items), f'Expected {len(items)} drawings, got {len(drawing_indices)}'
        for idx, d_i in enumerate(drawing_indices):
            item_num, char_str, zy_lines, test_type = items[idx]
            parts[d_i] = make_box_xml(100 + item_num, char_str, zy_lines, test_type, is_answer_sheet)
        new_doc_xml = ''.join(parts)

        temp_path = docx_path + '.tmp'
        with zipfile.ZipFile(temp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == 'word/document.xml':
                    zout.writestr(item, new_doc_xml.encode('utf-8'))
                elif item.filename == 'word/_rels/document.xml.rels':
                    rels_xml = zin.read(item.filename).decode('utf-8')
                    rels_xml = re.sub(r'<Relationship[^>]+Target="media/image\d+\.png"[^>]*/>', '', rels_xml)
                    zout.writestr(item, rels_xml.encode('utf-8'))
                elif re.match(r'word/media/image\d+\.png$', item.filename):
                    continue
                else:
                    zout.writestr(item, zin.read(item.filename))
    os.replace(temp_path, docx_path)
