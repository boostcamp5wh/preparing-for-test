def solution(new_id):
    new_id=''.join([c if c.isalpha() or c.isdigit() or c in ['-', '_', '.'] else '' for i, c in enumerate(list(new_id.lower()))])
    while '..' in new_id: new_id=new_id.replace('..', '.')
    new_id=list(new_id)
    if new_id[0]=='.': new_id[0]=''
    if new_id[-1]=='.': new_id[-1]=''
    new_id=''.join(new_id)
    if not new_id: new_id+='aaa'
    if len(new_id)>15:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=list(new_id)
            new_id[-1]=''
            new_id=''.join(new_id)
    while len(new_id)<3: new_id+=new_id[-1]
    return new_id
