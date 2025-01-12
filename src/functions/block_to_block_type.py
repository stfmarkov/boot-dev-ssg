from functools import reduce

def block_to_block_type(block):
    
    def check_heading(block):
        return block.startswith('#')
    
    def check_code(block):
        return block.startswith('```') and block.endswith('```')
    
    def check_quote(block):
        for line in block.split('\n'):
            if not line.startswith('>'):
                return False
        return True

    
    def check_unordered_list(block):
        for line in block.split('\n'):
            if not line.startswith('* '):
                return False
        return True
    
    def check_ordered_list(block):
        for idx, line in enumerate(block.split('\n')):
            is_numeral = line.split('. ')[0].isdigit()
            if (not is_numeral):
                return False
            is_next_numeral = int(line.split('. ')[0]) == idx + 1
            if not is_next_numeral:
                return False
        
        return True

    if check_heading(block):
        return 'heading'
    
    if check_code(block):
        return 'code'
    
    if check_quote(block):
        return 'quote'
    
    if check_unordered_list(block):
        return 'unordered_list'
    
    if check_ordered_list(block):
        return 'ordered_list'
    
    return 'paragraph'
