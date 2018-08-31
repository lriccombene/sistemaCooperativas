select asoc.id as asoc_id, pp.apellido, pp.nombre ,obs.tipo,
(select sum(pesos) from capital_suscripto where id_asoc = asoc.id) as capital_suscripto,
(select sum(pesos) from capital_integracion where id_asoc = asoc.id) as capital_integracion
from party_party pp
left join asociado as asoc on pp.id = asoc.id_party
left join observaciones as obs on asoc.id = obs.id_asoc
where obs.tipo IS NULL
