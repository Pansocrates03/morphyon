class Attributes:
    def __init__(self, attObj = {}):
        self.accept = None
        self.accept_charset = None
        self.acceskey = None
        self.action = None
        self.align = None
        self.alt = None
        #self.async = None
        self.autocomplete = None
        self.autofocus = None
        self.autoplay = None
        #self.bgcolor = None
        #self.border = None
        self.checked = None
        self.cite = None
        self.class_name = None ######33 CAMBIAR A "CLASS"
        #self.color = None
        self.cols = None
        self.colspan = None
        self.content = None
        self.contenteditable = None
        self.controls = None
        self.coords = None
        self.data = None
        #self.data-* ???
        self.datetime = None
        self.default = None
        self.defer = None
        self.dir = None
        self.dirname = None
        self.disabled = None
        self.download = None
        self.draggable = None
        self.enctype = None
        self.enterkeyhint = None
        self.for_attr = None ###### CAMBIAR A "FOR"
        self.form = None
        self.formaction = None
        self.headers = None
        self.height = None
        self.hidden = None
        self.high = None
        self.href = None
        self.hreflang = None
        self.http_equiv = None
        self.id = None
        self.inert = None
        self.inputmode = None
        self.ismap = None
        self.kind = None
        self.label = None
        self.lang = None
        self.list = None
        self.loop = None
        self.low = None
        self.max = None
        self.maxlength = None
        self.media = None
        self.method = None
        self.name = None
        self.novalidate = None
        self.onabort = None
        self.onafterprint = None
        self.onbeforeprint = None
        self.onbeforeunload = None
        self.onblur = None
        self.oncanplay = None
        self.oncanplaythrough = None
        self.onchange = None
        self.onclick = None
        self.oncontextmenu = None
        self.oncopy = None
        self.oncuechange = None
        self.oncut = None
        self.ondblclick = None
        self.ondrag = None
        self.ondragend = None
        self.ondragenter = None
        self.ondragleave = None
        self.ondragover = None
        self.ondragstart = None
        self.ondrop = None
        self.ondurationchange = None
        self.onemptied = None
        self.onended = None
        self.onerror = None
        self.onfocus = None
        self.onhashchange = None
        self.oninput = None
        self.oninvalid = None
        self.onkeydown = None
        self.onkeypress = None
        self.onkeyup = None
        self.onload = None
        self.onloadeddata = None
        self.onloadedmetadata = None
        self.onloadstart = None
        self.onmousedown = None
        self.onmousemove = None
        self.onmouseout = None
        self.onmouseover = None
        self.onmouseup = None
        self.onmousewheel = None
        self.onoffline = None
        self.ononline = None
        self.onpagehide = None
        self.onpageshow = None
        self.onpaste = None
        self.onpause = None
        self.onplay = None
        self.onplaying = None
        self.onpopstate = None
        self.onprogress = None
        self.onratechange = None
        self.onreset = None
        self.onresize = None
        self.onScroll = None
        self.onSearch = None
        self.onseeked = None
        self.onseeking = None
        self.onselect = None
        self.onstalled = None
        self.onstorage = None
        self.onsubmit = None
        self.onsuspend = None
        self.ontimeupdate = None
        self.ontoggle = None
        self.onunload = None
        self.onvolumechange = None
        self.onwaiting = None
        self.onwheel = None
        self.open = None
        self.optimum = None
        self.pattern = None
        self.placeholder = None
        self.popover = None
        self.popovertarget = None
        self.popovertargetaction = None
        self.poster = None
        self.preload = None
        self.readonly = None
        self.rel = None
        self.required = None
        self.reversed = None
        self.rows = None
        self.rowspan = None
        self.sandbox = None
        self.scope = None
        self.selected = None
        self.shape = None
        self.size = None
        self.sizes = None
        self.span = None
        self.spellcheck = None
        self.src = None
        self.srcdoc = None
        self.srclang = None
        self.srcset = None
        self.start = None
        self.step = None
        self.style = None
        self.tabindex = None
        self.target = None
        self.title = None
        self.translate = None
        self.type = None
        self.usemap = None
        self.value = None
        self.width = None
        self.wrap = None

        for prop, value in attObj.items():  # Use .items() to iterate over key-value pairs
            if hasattr(self, prop): 
                setattr(self, prop, value)
            else: 
                raise ValueError(f"Property {prop} is not supported")


    
    def setAttribute(self, name, value):
        # Check if a the classname starts with a number
        if isinstance(value, str) and value[0].isdigit():
            print("ERROR: A Classname cannot start with a number")
            return self
        # Check if the attribute exists and add it
        if hasattr(self, name): setattr(self, name, value)
        else: raise ValueError(f"Attribute '{name}' is not supported.")
        return self
    
    def render(self):
        # Generate attributes string
        attList = []
        
        for prop, value in self.__dict__.items():
            if value is not None:
                attList.append(f'{prop.replace('class_name','class')}="{value}"')
        attStr = "".join(attList)
        return " "+attStr