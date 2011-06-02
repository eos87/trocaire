# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Contraparte.logo'
        db.alter_column('encuesta_contraparte', 'logo', self.gf('trocaire.thumbs.ImageWithThumbsField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Contraparte.logo'
        db.alter_column('encuesta_contraparte', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accesocontrolrecurso': {
            'Meta': {'object_name': 'AccesoControlRecurso'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recursos'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"}),
            'recursos_decide': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'recursos_decide'", 'blank': 'True', 'to': "orm['encuesta.Recurso']"})
        },
        'encuesta.accesoinformacion': {
            'Meta': {'object_name': 'AccesoInformacion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'quien_brinda': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.BrindanCapacitacion']", 'null': 'True', 'blank': 'True'}),
            'recibe_capacitacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accion': {
            'Meta': {'object_name': 'Accion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'encuesta.accionmejoraratencion': {
            'Meta': {'object_name': 'AccionMejorarAtencion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuales': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Accion']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'realizo_accion': ('django.db.models.fields.IntegerField', [], {}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.RecursoCuentaIns']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.accionprevencion': {
            'Meta': {'object_name': 'AccionPrevencion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accionprevvbg': {
            'Meta': {'object_name': 'AccionPrevVBG'},
            'accion_prevenir': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.AccionPrevencion']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'realizo_accion': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.accionvbg': {
            'Meta': {'object_name': 'AccionVBG'},
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'busca_alternativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invita_actividad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_nada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_problema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_sabe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'se_acerca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.accionvbgfuncionario': {
            'Meta': {'object_name': 'AccionVBGFuncionario'},
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.accionvbglider': {
            'Meta': {'object_name': 'AccionVBGLider'},
            'accion_prevenir': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.AccionPrevencion']", 'null': 'True', 'blank': 'True'}),
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'busca_alternativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invita_actividad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_nada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_problema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_sabe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'porque_no': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'se_acerca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ud_previene': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.aporta': {
            'Meta': {'object_name': 'Aporta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.asuntopublicovbg': {
            'Meta': {'object_name': 'AsuntoPublicoVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'resolverse_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ResolverVBG']", 'symmetrical': 'False'})
        },
        'encuesta.brindancapacitacion': {
            'Meta': {'object_name': 'BrindanCapacitacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.buscarayuda': {
            'Meta': {'object_name': 'BuscarAyuda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.calidadatencion': {
            'Meta': {'object_name': 'CalidadAtencion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_porque': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'no_porque2': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'propuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'propuesta2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'si_tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.TipoPropuesta']", 'null': 'True', 'blank': 'True'}),
            'si_tipo2': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'propuesta_negociada1'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['encuesta.TipoPropuesta']"}),
            'valor_servicio': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.calidadatencionfuncionario': {
            'Meta': {'object_name': 'CalidadAtencionFuncionario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'valor_servicio': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.causavbg': {
            'Meta': {'object_name': 'CausaVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cultura': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'desconocimiento': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influencia_medios': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'influencia_religion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'machismo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'mujer_objeto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tiene_derecho': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'tipo_educacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        'encuesta.comoafecta': {
            'Meta': {'object_name': 'ComoAfecta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.composicionhogar': {
            'Meta': {'object_name': 'ComposicionHogar'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuantos_hijos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuantos_viven': ('django.db.models.fields.IntegerField', [], {}),
            'entre0y6': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'entre18ymas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'entre7y17': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hijos0y6_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hijos0y6_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hijos18ymas_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hijos18ymas_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hijos7y17_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hijos7y17_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tiene_hijos': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tiene_pareja': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vive_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ViveCon']", 'symmetrical': 'False'})
        },
        'encuesta.comunicacionasertiva': {
            'Meta': {'object_name': 'ComunicacionAsertiva'},
            'actitud_pasiva': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'analizar': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificar': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'identificar_prioridad': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'negociacion_exitosa': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.NegociacionExitosa']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pido': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'encuesta.conceptoviolencia': {
            'Meta': {'object_name': 'ConceptoViolencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'hablande': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.HablanDe']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        'encuesta.conocimientoley': {
            'Meta': {'object_name': 'ConocimientoLey'},
            'adulto_dinero': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'adulto_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existe_ley': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joven_case': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'joven_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'lider_religioso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_castiga': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'mencione': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'padre_golpea': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'patron_acoso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'})
        },
        'encuesta.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'correo': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('trocaire.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'encuesta.corresponsabilidad': {
            'Meta': {'object_name': 'Corresponsabilidad'},
            'acompanar': ('django.db.models.fields.IntegerField', [], {}),
            'arreglar_cama': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuidar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'cuidar_ninos': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_compras': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_mandados': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ir_reuniones': ('django.db.models.fields.IntegerField', [], {}),
            'jalar_agua': ('django.db.models.fields.IntegerField', [], {}),
            'lavar': ('django.db.models.fields.IntegerField', [], {}),
            'lavar_trastes': ('django.db.models.fields.IntegerField', [], {}),
            'limpiar': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_lena': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pagar_servicios': ('django.db.models.fields.IntegerField', [], {}),
            'plancar': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.creencia': {
            'Meta': {'object_name': 'Creencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'escoger_amistades': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'esposa_obedece': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hombre_maltrata': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'problema_familiar': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quien_manda': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sexo_obligacion': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'encuesta.decision': {
            'Meta': {'object_name': 'Decision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.efectovbg': {
            'Meta': {'object_name': 'EfectoVBG'},
            'afecta_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'como_afecta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.ComoAfecta']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        'encuesta.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.expresionvbg': {
            'Meta': {'object_name': 'ExpresionVBG'},
            'amenaza_chantajes': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'estudio_varon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'golpe_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hombre_celoso': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marido_empuja': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'marido_no_valora': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mujer_divertirse': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mujer_participe': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'no_organizarte': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'obedecer_marido': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'palabras_miradas': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pedir_dinero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pedir_permiso': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'progreso_hombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'propiedades_hombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sexo_obligada': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sexo_sin_proteccion': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'encuesta.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'cuanto_tiempo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Institucion']"}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.hablande': {
            'Meta': {'object_name': 'HablanDe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.hombre': {
            'Meta': {'object_name': 'Hombre'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.incidenciapolitica': {
            'Meta': {'object_name': 'IncidenciaPolitica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existen_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'satisfecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.incidenciapoliticafuncionario': {
            'Meta': {'object_name': 'IncidenciaPoliticaFuncionario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'ha_recibido': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_comunidades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lugar.Comunidad']", 'null': 'True', 'blank': 'True'}),
            'que_propuestas': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'propuesta_negociada'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['encuesta.TipoPropuesta']"}),
            'tipo_propuestas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.TipoPropuesta']", 'null': 'True', 'blank': 'True'}),
            'ud_negociado': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.informacionsocioeconomica': {
            'Meta': {'object_name': 'InformacionSocioEconomica'},
            'aportan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Aporta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.LugarDeTrabajo']", 'null': 'True', 'blank': 'True'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hace_dinero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.informacionsocioeconomicafuncionario': {
            'Meta': {'object_name': 'InformacionSocioEconomicaFuncionario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.informacionsocioeconomicalider': {
            'Meta': {'object_name': 'InformacionSocioEconomicaLider'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.LugarDeTrabajo']", 'null': 'True', 'blank': 'True'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'encuesta.instrumento': {
            'Meta': {'object_name': 'Instrumento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.justificacionvbg': {
            'Meta': {'object_name': 'JustificacionVBG'},
            'comportamiento': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'creencias': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'drogas': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'estres': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influencia_familiar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'licor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'mujer_no_caso': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'nace_asi': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'pobreza': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'victima': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        'encuesta.lider': {
            'Meta': {'object_name': 'Lider'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'cuanto_tiempo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.lugardetrabajo': {
            'Meta': {'object_name': 'LugarDeTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.motivoparticipacion': {
            'Meta': {'object_name': 'MotivoParticipacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.mujer': {
            'Meta': {'object_name': 'Mujer'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'cuanto_tiempo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.negociacionexitosa': {
            'Meta': {'object_name': 'NegociacionExitosa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'encuesta.participacionpublica': {
            'Meta': {'object_name': 'ParticipacionPublica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'espacio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Espacio']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.MotivoParticipacion']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.prevalenciavbg': {
            'Meta': {'object_name': 'PrevalenciaVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.TipoVBG']", 'null': 'True', 'blank': 'True'}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.prevalenciavbghombre': {
            'Meta': {'object_name': 'PrevalenciaVBGHombre'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.TipoVBG']", 'null': 'True', 'blank': 'True'}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien2']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.prevalenciavbglider': {
            'Meta': {'object_name': 'PrevalenciaVBGLider'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'frecuencia2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ha_vivido_vbg2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'piensa_existe': ('django.db.models.fields.IntegerField', [], {}),
            'que_tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.TipoVBG']", 'null': 'True', 'blank': 'True'}),
            'que_tipo2': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tipovbg_ejercida'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['encuesta.TipoVBG']"}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien']", 'null': 'True', 'blank': 'True'}),
            'quien2': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuesta.Quien2']", 'null': 'True', 'blank': 'True'})
        },
        'encuesta.quedebehacer': {
            'Meta': {'object_name': 'QueDebeHacer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.quien': {
            'Meta': {'object_name': 'Quien'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.quien2': {
            'Meta': {'object_name': 'Quien2'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'encuesta.recursocuentains': {
            'Meta': {'object_name': 'RecursoCuentaIns'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'encuesta.registrodato': {
            'Meta': {'object_name': 'RegistroDato'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuantos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'emocional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'fisica': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lleva_registro': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'otro': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'sexual': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'sicologica': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'encuesta.resolvervbg': {
            'Meta': {'object_name': 'ResolverVBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.rutacritica': {
            'Meta': {'object_name': 'RutaCritica'},
            'centro_mujeres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'centro_salud': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comisaria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrumentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Instrumento']", 'symmetrical': 'False'}),
            'juzgado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ministerio_publico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pasos': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'encuesta.situacionvbg': {
            'Meta': {'object_name': 'SituacionVBG'},
            'conoce_hombres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conoce_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.solucionconflicto': {
            'Meta': {'object_name': 'SolucionConflicto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.tipopropuesta': {
            'Meta': {'object_name': 'TipoPropuesta'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'encuesta.tipovbg': {
            'Meta': {'object_name': 'TipoVBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.tomadecision': {
            'Meta': {'object_name': 'TomaDecision'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Decision']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.vivecon': {
            'Meta': {'object_name': 'ViveCon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']", 'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['encuesta']
