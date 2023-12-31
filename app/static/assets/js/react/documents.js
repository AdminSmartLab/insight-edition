// ! React

const INITIAL_DATA = JSON.parse(document.getElementById('initialData').textContent)
const CHOICES = JSON.parse(document.getElementById('choices').textContent)
const CSRF_TOKEN = document.getElementsByName('csrfmiddlewaretoken')[0].value
const TODAY = new Date().toISOString().split("T")[0]


const Portlet = ({
  title,
  handler,
  children,
  display="in"
}) => {
  return (
    <div className="row">
    <div className="col-md-12">
      <div className="portlet">
        <div className="portlet-heading bg-info">
            <h3 className="portlet-title">{title}</h3>
            <div className="portlet-widgets">
                <a data-toggle="collapse" data-parent={`#accordion-${handler}`} href={`#portlet-${handler}`}><i className="fa fa-minus"></i></a>
            </div>
            <div className="clearfix"></div>
        </div>
        <div id={`portlet-${handler}`} className={`panel-collapse collapse ${display}`}>
            <div className="portlet-body">
              {children}
            </div>
        </div>
      </div>             
    </div>
  </div>
  )
}


const Encabezado = ({
    documento,
    setDocumento,
    onlyRead,
    }) => {

    const types = Object.keys(CHOICES.receipt.receipt_type)
    const point_of_sales = CHOICES.receipt.point_of_sales && Object.keys(CHOICES.receipt.point_of_sales)

    const reload = (e)=> {
        let param = e.target.name
        if (param.split('.').length > 1) param = param.split('.')[1]
        const value = e.target.value
        var URL = document.URL;
        var NEW = `${param}=${value}`;
        if(URL.indexOf(param) != -1) {
          var PARAMETER = URL.split("&").filter((par)=> par.indexOf(param) != -1)[0]
          URL = URL.replace(PARAMETER, NEW)
        }
        else {
          URL = URL + "&" + NEW
        }
        window.location = URL;
    }

    const handleChange = (e) => {
      const name = e.target.name
      const subfields = name.split(".")
      subfields.length > 1 ?
        setDocumento({
          ...documento,
          [subfields[0]]: {
            ...documento[subfields[0]],
            [subfields[1]]: e.target.value
          }
        }) :
        setDocumento({
          ...documento,
          [name]: e.target.value
        })
    }

    return (
        <Portlet title="Encabezados" handler='encabezados'>
          <div className="row">
            <div className="col-md-2">
              <label htmlFor="receipt.receipt_type">Tipo</label>
              <select 
                className="form-control" 
                name="receipt.receipt_type" 
                id="receipt.receipt_type" 
                onChange={reload}
                value={documento.receipt.receipt_type || ''}
                >
                <option value=''> --- </option>
                {types.map((type, i) => (
                    <option key={i} value={type}>{type}</option>
                ))}
              </select>
            </div>
            <div className="col-md-2">
              <label htmlFor="receipt.point_of_sales">Punto Vta</label>
              {point_of_sales ? <select 
              className="form-control"
              name="receipt.point_of_sales" 
              id="receipt.point_of_sales" 
              onChange={handleChange}
              value={documento.receipt.point_of_sales || ''}
            >
              <option value=''> --- </option>
                {point_of_sales.map((point, i) => (
                    <option key={i} value={point}>{point}</option>
                ))}
              </select> : 
                 <input 
                 type="number" 
                 className="form-control" 
                 name="receipt.point_of_sales" 
                 id="receipt.point_of_sales"
                 min="0" 
                 onChange={handleChange}
                 value={documento.receipt.point_of_sales || ''}
               />           
              
              
              }
              
            </div>            
            <div className="col-md-2">
              <label htmlFor="receipt.receipt_number">N°</label>
              <input 
                type="number" 
                className="form-control" 
                disabled={
                  (CHOICES.module_handler === "documento_cliente") || 
                  (documento.receipt && ["Orden de Pago X", "Transferencia X"].indexOf(documento.receipt.receipt_type) === 0)
                }
                name="receipt.receipt_number" 
                id="receipt.receipt_number" 
                onChange={handleChange}
                value={documento.receipt.receipt_number || ''}
              />
            </div>              
            <div className="col-md-2">
              <label htmlFor="receipt.issued_date">Fecha Cbte.</label>
              <input 
                className="form-control" 
                name="receipt.issued_date" 
                type="date" 
                onChange={handleChange}
                value={documento.receipt.issued_date || ''}
              />
            </div>               
            <div className="col-md-2">
              <label htmlFor="fecha_operacion">Fecha Op.</label>
              <input 
                className="form-control" 
                name="fecha_operacion" 
                type="date" 
                onChange={reload}
                value={documento.fecha_operacion || ''}
              />
            </div>                    
          </div>
        </Portlet>
    )
};



const Appendable = ({ documento, setDocumento, onlyRead, title, handler, fields, cleanedField }) => {

  const [grouped, setGrouped] = React.useState([...documento[handler], cleanedField])

  React.useEffect(() => {
    setDocumento(() => ({
      ...documento,
      [handler]: grouped
    }))

  }, [grouped])

  const handleChange = (e) => {
    e.preventDefault()
    const [row, name] = e.target.name.split('.')
    setGrouped(() => {
      grouped[row][name] = e.target.value
      return [...grouped]
    })
  }

  const AppendCleanFieldsGroup = (e) => {
    e.preventDefault()
    setGrouped((groups) => ([...groups, cleanedField]))
  }
  const RemoveLastFieldsGroup = (e) => {
    e.preventDefault()
    const lastElement = grouped.length-1
    if (lastElement >= 1) {
      setGrouped((groups) => ([...groups.filter((_, i) => i !== lastElement)]))
    }
  }




  const renderField = (field, value, fi) => {
    switch (field.type) {
      case 'select':
        return <select className="form-control input-sm" name={`${fi}.${field.name}`} value={value || ''} onChange={handleChange}>
          <option value=''> --- </option>
          {Object.keys(field.choices).map((c, i) => (
            <option key={i} value={c}>{field.choices[c]}</option>
          ))}
        </select>
      case 'date':
        return <input className="form-control input-sm" type="date" name={`${fi}.${field.name}`} value={value || ''} onChange={handleChange} />
      case 'text':
        return <input className="form-control input-sm" type="text" name={`${fi}.${field.name}`} value={value || ''} onChange={handleChange} />
      case 'number':
        return <input className="form-control input-sm" type="number" name={`${fi}.${field.name}`} value={value || ''} onChange={handleChange} />        
      default:
        break;
    }
  }

  return (
    <Portlet title={title} handler={handler}>
      <div className="row">
        <div className="col-md-12">
          <table className="table table-condensed">
            <thead>
              <tr>
                {fields.map((field, i) => (<th key={i}>
                  {field.label}
                </th>))}
              </tr>
            </thead>
            <tbody>
              {grouped.map((fieldset, fi) => (
                <tr key={fi}>
                {fields.map((field, i) =>(
                  <td key={i}>
                    {renderField(field, fieldset[field.name], fi)}
                  </td>
                ))}
                </tr>
              ))}

            </tbody>
          </table>
        </div>            
        <div className="col-md-offset-6 text-right">
          <button onClick={RemoveLastFieldsGroup} className="btn btn-sm btn-danger text-right"><span className="fa fa-minus"></span></button>
          <button onClick={AppendCleanFieldsGroup} className="btn btn-sm btn-success text-right"><span className="fa fa-plus"></span></button>
        </div>
      </div>
    </Portlet>
)  
};

const Selectable = ({ documento, setDocumento, onlyRead, title, handler, rows }) => {

  const [grouped, setGrouped] = React.useState(
    Object.entries(rows).map(obj=> ({
        vinculo: obj[0], 
        monto:obj[1].monto, 
        checked:false,
        descripcion: obj[1].descripcion
      }))
  )

  const titles = Object.keys(Object.entries(rows)[0][1])

  const handleChange = (e) => {
    e.preventDefault()
    const [row, name] = e.target.name.split('.')
    setGrouped(() => {
      if (name === "vinculo") {
        grouped[row]['checked'] = !grouped[row]['checked']
      } else {
        grouped[row][name] = e.target.value
      }
      return [...grouped]
    })
  }

  React.useEffect(() => {
    setDocumento(() => ({
      ...documento,
      [handler]: grouped.filter(g => (g.monto > 0 && g.checked === true))
    }))

  }, [grouped])


  return (
    <Portlet title={title} handler={handler} display={(["utilizaciones_disponibilidades", "utilizaciones_saldos"].includes(handler) ? "" : "in")}>
      <div className="row">
        <div className="col-md-12">
          <table className="table table-condensed table-responsive">
            <thead>
              <tr>
                <th></th>
                {titles.map((t, i) => (<th key={i}>{t}</th>))}
              </tr>
            </thead>
            <tbody>
              {grouped.map((row, i) => {
                return (<tr key={i}>
                  <td>
                    <input 
                      className="form-control input-sm" 
                      type="checkbox" 
                      value={row.vinculo} 
                      name={`${i}.vinculo`} 
                      checked={row.checked} 
                      onChange={handleChange}
                    />
                  </td>
                  <td>{row.descripcion}</td>
                  <td>
                    <input 
                      className="form-control input-sm" 
                      type="number" 
                      value={row.monto} 
                      name={`${i}.monto`} 
                      onChange={handleChange}
                    />
                  </td>
                </tr>)
              })}

            </tbody>
          </table>
        </div>
      </div>
    </Portlet>
)  
};


const Comprobante = ({ initialData, onlyRead }) => {
    var URL = document.URL
    let queryParams 
    if((URL).indexOf('?') != -1) {
      var search = location.search.substring(1);
      queryParams = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}')
    }
    let fieldsLists = {}
    Object.keys(initialData).forEach(field => {
      if (initialData[field] instanceof Array) {
        fieldsLists[field] = initialData[field]
      }
      
    })

    const [documento, setDocumento] = React.useState({
        id: initialData ? initialData.id : null,
        fecha_operacion: (queryParams && queryParams.fecha_operacion) ? 
          queryParams.fecha_operacion : 
          initialData.fecha_operacion ? 
          initialData.fecha_operacion : 
          TODAY,
        descripcion: '',
        receipt: {
          receipt_type: (queryParams && queryParams.receipt_type) ? queryParams.receipt_type : initialData.receipt.receipt_type,
          point_of_sales: initialData.receipt.point_of_sales ? initialData.receipt.point_of_sales : '',
          issued_date: initialData.receipt.issued_date ? initialData.receipt.issued_date : TODAY,
          receipt_number: initialData.receipt.receipt_number ? initialData.receipt.receipt_number : '',
        },
        ...fieldsLists
      });

    const [canSend, setCanSend] = React.useState(false)
  
    React.useEffect(() => {

      let cantSend = true
      if (documento.receipt.receipt_type && documento.receipt.point_of_sales) {
        
        // Si hay creditos significa que es una Factura a cliente
        if (documento.creditos && documento.creditos.length > 0) {
          const incomplete = documento.creditos.filter(c => (c.destinatario === "" || c.concepto === "" || c.monto === "" || c.monto == 0))
          incomplete.length > 0 ? cantSend = true : cantSend = false
        }

        // Si hay cobros significa que es un Recibo o una Nota de Credito
        if (documento.cobros) {
          const totalCobros = documento.cobros.reduce((total, current) => total + Number(current['monto']), 0)
          
          // Si hay resultados significa que es una Nota de Credito
          if (documento.resultados) {
            const totalResultados = documento.resultados.filter(r => r.cuenta !== "").reduce((total, current) => total + Number(current['monto']), 0)
            totalCobros > 0 && totalCobros === totalResultados ? cantSend = false : cantSend = true
          }

          // Si hay cajas significa que es un Recibo
          if (documento.cajas) {

          }
        }
      } 
      if (cantSend) {
        setCanSend(false)
      } else {
        setCanSend(true)
      }

    }, [documento])
    
    const handleSubmit = React.useCallback((event) => {
      setCanSend(false)
      event.preventDefault();
      window.fetch(document.form_cbte.action, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": CSRF_TOKEN,
        },
        body: JSON.stringify(documento),
      }).then(response => {
        if (response.redirected) {
          window.location = response.url
        }
      })
    },[documento]);

    const handleBack = (e) => {
      history.back()
    }
    return (
      <form onSubmit={handleSubmit} name="form_cbte" method="POST">
        <Encabezado 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
        />

        {/* Clientes: Seccion de Creditos */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.creditos && <Appendable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Creditos"
          handler="creditos"
          fields={[
            {
              type: 'select',
              name: 'destinatario',
              label: 'Destinatario',
              choices: CHOICES.creditos.destinatario
            },
            {
              type: 'select',
              name: 'concepto',
              label: 'Concepto',
              choices: CHOICES.creditos.concepto
            },
            {
              type: 'date',
              name: 'periodo',
              label: 'Periodo',
            },
            {
              type: 'date',
              name: 'fecha_gracia',
              label: 'Descuento',
            },            
            {
              type: 'date',
              name: 'fecha_vencimiento',
              label: 'Vencimiento',
            },
            {
              type: 'text',
              name: 'detalle',
              label: 'Detalle',
            },
            {
              type: 'number',
              name: 'cantidad',
              label: 'Cantidad',
            },            
            {
              type: 'number',
              name: 'monto',
              label: 'Monto',
            },                        
          ]}
          cleanedField={{
            destinatario: '',
            concepto: '',
            periodo: TODAY,
            fecha_gracia: TODAY,
            fecha_vencimiento: TODAY,
            detalle: '',
            cantidad: 0,
            monto: 0,
          }}
          />
        }

        {/* Clientes: Seccion de Creditos */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.debitos && <Appendable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Debitos"
          handler="debitos"
          fields={[
            {
              type: 'select',
              name: 'cuenta',
              label: 'Cuenta',
              choices: CHOICES.debitos.cuenta
            },
            {
              type: 'date',
              name: 'periodo',
              label: 'Periodo',
            },       
            {
              type: 'date',
              name: 'fecha_vencimiento',
              label: 'Vencimiento',
            },
            {
              type: 'text',
              name: 'detalle',
              label: 'Detalle',
            },
          
            {
              type: 'number',
              name: 'monto',
              label: 'Monto',
            },                        
          ]}
          cleanedField={{
            destinatario: '',
            concepto: '',
            periodo: TODAY,
            fecha_gracia: TODAY,
            fecha_vencimiento: TODAY,
            detalle: '',
            cantidad: 0,
            monto: 0,
          }}
          />
        }        

        {/* Clientes: Seccion de Cobros */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.cobros && <Selectable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Items pendientes de cobro"
          handler="cobros"
          rows={CHOICES.cobros.vinculo}
          />
        }        

        {/* Proveedores: Seccion de Deudas */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.pagos && <Selectable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Items pendientes de pago"
          handler="pagos"
          rows={CHOICES.pagos.vinculo}
          />
        }              

        {/* Seccion de Cajas */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.cajas && <Appendable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Formas de pago"
          handler="cajas"
          fields={[
            {
              type: 'select',
              name: 'cuenta',
              label: 'Cuenta',
              choices: CHOICES.cajas.cuenta
            },
            {
              type: 'text',
              name: 'detalle',
              label: 'Detalle',
            },                 
            {
              type: 'date',
              name: 'fecha_vencimiento',
              label: 'Vencimiento',
            },          
            {
              type: 'number',
              name: 'monto',
              label: 'Monto',
            },                        
          ]}
          cleanedField={{
            cuenta: '',
            detalle: '',
            fecha_vencimiento: '',
            monto: 0,
          }}
          />
        }

        {/* Seccion de Resultados */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.resultados && <Appendable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Resultados a generar"
          handler="resultados"
          fields={[
            {
              type: 'select',
              name: 'cuenta',
              label: 'Cuenta',
              choices: CHOICES.resultados.cuenta
            },
            {
              type: 'text',
              name: 'detalle',
              label: 'Detalle',
            },                 
            {
              type: 'date',
              name: 'periodo',
              label: 'Período',
            },          
            {
              type: 'number',
              name: 'monto',
              label: 'Monto',
            },                        
          ]}
          cleanedField={{
            cuenta: '',
            detalle: '',
            periodo: TODAY,
            monto: 0,
          }}
          />
        }    

        {/* Seccion de Utilización de saldos */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.utilizaciones_saldos && Object.keys(CHOICES.utilizaciones_saldos).length > 0 && <Selectable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Utilizar saldos anteriores"
          handler="utilizaciones_saldos"
          rows={CHOICES.utilizaciones_saldos.vinculo}
          />
        }   

        {/* Seccion de Utilización de disponibilidades */}
        {Object.keys(fieldsLists).length > 0 && fieldsLists.utilizaciones_disponibilidades && Object.keys(CHOICES.utilizaciones_disponibilidades).length > 0 && <Selectable 
          documento={documento} 
          setDocumento={setDocumento} 
          onlyRead={onlyRead}
          title="Utilizar disponibilidades"
          handler="utilizaciones_disponibilidades"
          rows={CHOICES.utilizaciones_disponibilidades.vinculo}
          />
        }                  

            
        {documento.receipt.receipt_type && documento.fecha_operacion && <Portlet 
          title="Descripción"
          handler="descripcion">
          <div className="row">
            <div className="col-md-12">
              
              <textarea 
                type="text" 
                id='descripcion' 
                name="descripcion" 
                className="form-control" 
                value={documento.descripcion || ''}
                onChange={(e) => setDocumento({...documento, descripcion: e.target.value})}
              />
            </div>            
          </div>                        
        </Portlet>}

  
        {/* {!onlyRead && 
          <Contado 
          documento={documento}     
          setDocumento={setDocumento}
          onlyRead={onlyRead} />
        } */}
        
        <div className="panel-footer">
          <div className="row">
            <div className="col-xs-6">
              <button onClick={handleBack} className="btn btn-bordered btn-default btn-block">Cancelar</button>
            </div>
            <div className="col-xs-6">
              <button disabled={!canSend} onClick={handleSubmit} className="btn btn-bordered btn-primary btn-block">Guardar</button>
            </div>
          </div>
        </div>
      </form>
    );
  };


const app = document.querySelector('#app')

ReactDOM.createRoot(
    app
).render(
    <Comprobante initialData={INITIAL_DATA} onlyRead={false} />
)